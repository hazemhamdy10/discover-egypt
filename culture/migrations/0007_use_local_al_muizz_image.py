from django.db import migrations


def use_local_al_muizz_image(apps, schema_editor):
    Destination = apps.get_model("culture", "Destination")
    Destination.objects.filter(slug="al-muizz-street").update(
        image_url="/static/culture/images/al-muizz-street.svg"
    )


class Migration(migrations.Migration):
    dependencies = [("culture", "0006_fix_broken_glass_image")]
    operations = [migrations.RunPython(use_local_al_muizz_image, migrations.RunPython.noop)]
