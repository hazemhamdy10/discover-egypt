"""Render the Django site to static HTML for Netlify.

Netlify does not run Python servers, so this script runs at build time:
it builds a throwaway in-memory SQLite database from the project's migrations (which
seed all of the site's content), renders every public page with Django's
test client, and writes the HTML plus collected static files to ``dist/``.

Usage: python netlify_build.py
"""

import os
import shutil
import sys
from pathlib import Path
from urllib.parse import unquote

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "dist"

# Build against a local SQLite database seeded by migrations, with production
# settings (no debug pages, hashed static file names).
os.environ.pop("DATABASE_URL", None)
os.environ["DEBUG"] = "False"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
sys.path.insert(0, str(BASE_DIR))

import django  # noqa: E402
from django.conf import settings  # noqa: E402

# Use an in-memory database so a local db.sqlite3 is never touched.
settings.DATABASES["default"] = {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}
django.setup()

from django.core.management import call_command  # noqa: E402
from django.test import Client  # noqa: E402
from django.urls import reverse  # noqa: E402

from culture.models import Article, Craft, Destination  # noqa: E402


def page_urls():
    yield reverse("culture:home")
    yield reverse("culture:articles")
    yield reverse("culture:destinations")
    yield reverse("culture:crafts")
    for article in Article.objects.filter(status="published"):
        yield reverse("culture:article_detail", args=[article.slug])
    for destination in Destination.objects.all():
        yield reverse("culture:destination_detail", args=[destination.slug])
    for craft in Craft.objects.all():
        yield reverse("culture:craft_detail", args=[craft.slug])


def write(relative_path, content):
    target = OUTPUT_DIR / relative_path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(content)


def main():
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)

    call_command("migrate", interactive=False, verbosity=1)
    call_command("collectstatic", interactive=False, clear=True, verbosity=1)

    client = Client(SERVER_NAME="localhost")
    count = 0
    for url in page_urls():
        response = client.get(url)
        if response.status_code != 200:
            raise SystemExit(f"Rendering {url} failed with HTTP {response.status_code}")
        write(Path(unquote(url).strip("/")) / "index.html", response.content)
        count += 1

    not_found = client.get("/__netlify-404__/")
    write("404.html", not_found.content)

    # Publish only what the static site serves: skip Django admin assets (the
    # admin can't run on a static host), WhiteNoise's pre-compressed .gz copies
    # (Netlify compresses responses itself) and the internal manifest file.
    static_out = OUTPUT_DIR / settings.STATIC_URL.strip("/")
    static_out.mkdir(parents=True, exist_ok=True)
    for entry in Path(settings.STATIC_ROOT).iterdir():
        if entry.name in ("admin", "staticfiles.json"):
            continue
        if entry.is_dir():
            shutil.copytree(entry, static_out / entry.name, ignore=shutil.ignore_patterns("*.gz"))
        elif not entry.name.endswith(".gz"):
            shutil.copy2(entry, static_out / entry.name)
    media_root = Path(settings.MEDIA_ROOT)
    if media_root.is_dir():
        shutil.copytree(media_root, OUTPUT_DIR / settings.MEDIA_URL.strip("/"))

    print(f"Rendered {count} pages to {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
