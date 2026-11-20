from django.db import migrations


def make_topic_images_unique(apps, schema_editor):
    Article = apps.get_model("culture", "Article")
    Destination = apps.get_model("culture", "Destination")

    Article.objects.filter(slug="nubian-art").update(
        image_url="https://images.unsplash.com/photo-1528127269322-539801943592?auto=format&fit=crop&w=1200&q=85"
    )
    Article.objects.filter(slug="egyptian-festivals").update(
        image_url="https://images.unsplash.com/photo-1514525253161-7a46d19cd819?auto=format&fit=crop&w=1200&q=85"
    )
    Article.objects.filter(slug="egyptian-cotton").update(
        image_url="https://images.unsplash.com/photo-1523381210434-271e8be1f52b?auto=format&fit=crop&w=1200&q=85"
    )

    Destination.objects.filter(slug="al-muizz-street").update(
        image_url="https://images.unsplash.com/photo-1539650116574-75c0c6d73f6e?auto=format&fit=crop&w=1200&q=85"
    )
    Destination.objects.filter(slug="wadi-al-hitan").update(
        image_url="https://images.unsplash.com/photo-1469474968028-56623f02e42e?auto=format&fit=crop&w=1200&q=85"
    )


class Migration(migrations.Migration):
    dependencies = [("culture", "0004_replace_random_images")]
    operations = [migrations.RunPython(make_topic_images_unique, migrations.RunPython.noop)]
