from django.db import migrations


def replace_images(apps, schema_editor):
    Article = apps.get_model("culture", "Article")
    Destination = apps.get_model("culture", "Destination")
    Craft = apps.get_model("culture", "Craft")

    pyramid = "https://images.unsplash.com/photo-1663192365262-ae9f884ac8b6?auto=format&fit=crop&w=1200&q=85"
    food = "https://images.unsplash.com/photo-1547592180-85f173990554?auto=format&fit=crop&w=1200&q=85"
    music = "https://images.unsplash.com/photo-1524368535928-5b5e00ddc76b?auto=format&fit=crop&w=1200&q=85"
    textile = "https://pulitzercenter.org/sites/default/files/EgyptEntrepreuners.jpg"
    pottery = "https://exposure.accelerator.net/production/photos/9yjtj3txnnhr3skc0i7jqgvu454x2z8udygk/original.jpg"
    library = "https://images.unsplash.com/photo-1722900265028-e701d3f4b8c2?auto=format&fit=crop&w=1200&q=85"
    desert = "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=1200&q=85"
    jewelry = "https://images.unsplash.com/photo-1617038220319-276d3cfab638?auto=format&fit=crop&w=1200&q=85"
    wood = "https://images.unsplash.com/photo-1544967082-d9d25d867d66?auto=format&fit=crop&w=1200&q=85"
    glass = "https://images.unsplash.com/photo-1577083552431-6e5fd01988f5?auto=format&fit=crop&w=1200&q=85"

    Article.objects.filter(slug="nubian-art").update(image_url=textile)
    Article.objects.filter(slug="egyptian-cuisine").update(image_url=food)
    Article.objects.filter(slug="egyptian-music").update(image_url=music)
    Article.objects.filter(slug="egyptian-festivals").update(image_url=textile)
    Article.objects.filter(slug="egyptian-cotton").update(image_url=textile)

    Destination.objects.filter(slug__in=["al-muizz-street", "qurna-luxor"]).update(image_url=pyramid)
    Destination.objects.filter(slug="alexandria-corniche").update(image_url=library)
    Destination.objects.filter(slug="wadi-al-hitan").update(image_url=desert)
    Destination.objects.filter(slug="siwa-oasis").update(image_url=desert)

    Craft.objects.filter(slug__in=["egyptian-pottery"]).update(image_url=pottery)
    Craft.objects.filter(slug="handwoven-textiles").update(image_url=textile)
    Craft.objects.filter(slug="egyptian-jewelry").update(image_url=jewelry)
    Craft.objects.filter(slug="egyptian-woodwork").update(image_url=wood)
    Craft.objects.filter(slug="stained-glass").update(image_url=glass)


class Migration(migrations.Migration):
    dependencies = [("culture", "0003_expand_content_and_images")]
    operations = [migrations.RunPython(replace_images, migrations.RunPython.noop)]
