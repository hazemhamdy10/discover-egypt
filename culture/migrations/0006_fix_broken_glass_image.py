from django.db import migrations


def fix_glass_image(apps, schema_editor):
    Craft = apps.get_model("culture", "Craft")
    Craft.objects.filter(slug="stained-glass").update(
        image_url="https://images.unsplash.com/photo-1529908537380-8f8999f17a39?auto=format&fit=crop&w=1200&q=85"
    )


class Migration(migrations.Migration):
    dependencies = [("culture", "0005_make_topic_images_unique")]
    operations = [migrations.RunPython(fix_glass_image, migrations.RunPython.noop)]
