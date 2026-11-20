from django.db import migrations


def seed_content(apps, schema_editor):
    Article = apps.get_model("culture", "Article")
    Destination = apps.get_model("culture", "Destination")
    Craft = apps.get_model("culture", "Craft")

    Article.objects.get_or_create(
        slug="nubian-art",
        defaults={
            "title": "حكاية الفن النوبي وألوان الجنوب",
            "category": "arts",
            "summary": "ألوان زاهية وحكايات متوارثة تلخص روح النوبة ودفء مجتمعها.",
            "content": "يعبّر الفن النوبي عن علاقة الإنسان بالمكان والنيل. تظهر الألوان والرموز في البيوت والمشغولات لتحكي قصصًا من الذاكرة اليومية وتحتفي بالضيافة والانتماء.",
            "status": "published",
        },
    )
    Article.objects.get_or_create(
        slug="egyptian-cuisine",
        defaults={
            "title": "المطبخ المصري: ذاكرة على المائدة",
            "category": "food",
            "summary": "أطباق بسيطة تجمع العائلة وتحمل أثر المدن والقرى المصرية.",
            "content": "من الكشري إلى الفول والطعمية، يروي المطبخ المصري حكاية التنوع والتكافل. تتغير الوصفات من منطقة إلى أخرى، لكن تبقى المائدة مساحة للكرم والاحتفال.",
            "status": "published",
        },
    )
    Destination.objects.get_or_create(
        slug="al-muizz-street",
        defaults={
            "name": "شارع المعز لدين الله الفاطمي",
            "governorate": "القاهرة",
            "description": "متحف مفتوح يضم مساجد وبيوتًا وأسواقًا تاريخية في قلب القاهرة القديمة.",
            "cultural_significance": "يمثل الشارع طبقات متعاقبة من العمارة والفنون الإسلامية، وما زال نابضًا بالحرف والأسواق.",
            "best_time_to_visit": "من أكتوبر إلى أبريل، ويفضل بعد العصر.",
        },
    )
    Destination.objects.get_or_create(
        slug="qurna-luxor",
        defaults={
            "name": "القرنة ووادي الملوك",
            "governorate": "الأقصر",
            "description": "منطقة أثرية فريدة على الضفة الغربية لنهر النيل تضم مقابر ومعابد ملكية.",
            "cultural_significance": "تكشف المنطقة عن تصور المصريين القدماء للحياة والخلود وفنون الكتابة والرسم.",
            "best_time_to_visit": "من نوفمبر إلى مارس، في الصباح الباكر.",
        },
    )
    Craft.objects.get_or_create(
        slug="egyptian-pottery",
        defaults={
            "name": "الخزف المصري",
            "category": "pottery",
            "origin": "قرى الفسطاط وسوهاج",
            "description": "حرفة تعتمد على تشكيل الطين وتحويله إلى أوانٍ وقطع فنية تحمل بصمة الصانع.",
            "materials": "الطين الطبيعي، الألوان المعدنية، وطلاء زجاجي.",
            "production_process": "يُشكّل الطين، ثم يُجفف ويُحرق في أفران خاصة قبل تلوينه وحرقه مرة أخرى.",
            "artisan_information": "تنتقل أسرار الحرفة بالتدريب والممارسة من جيل إلى جيل.",
        },
    )
    Craft.objects.get_or_create(
        slug="handwoven-textiles",
        defaults={
            "name": "النسيج اليدوي",
            "category": "textiles",
            "origin": "أخميم وسيوة",
            "description": "منسوجات يدوية تجمع بين الخامات الطبيعية والزخارف المستوحاة من البيئة.",
            "materials": "القطن والصوف وأصباغ طبيعية.",
            "production_process": "تُجهز الخيوط ثم تُنسج على النول اليدوي وتُضاف الزخارف بعناية.",
            "artisan_information": "تمنح الحرفة النساء والشباب فرصة للحفاظ على التراث ودعم الدخل المحلي.",
        },
    )


def remove_seed_content(apps, schema_editor):
    apps.get_model("culture", "Article").objects.filter(
        slug__in=["nubian-art", "egyptian-cuisine"]
    ).delete()
    apps.get_model("culture", "Destination").objects.filter(
        slug__in=["al-muizz-street", "qurna-luxor"]
    ).delete()
    apps.get_model("culture", "Craft").objects.filter(
        slug__in=["egyptian-pottery", "handwoven-textiles"]
    ).delete()


class Migration(migrations.Migration):
    dependencies = [("culture", "0001_initial")]
    operations = [migrations.RunPython(seed_content, remove_seed_content)]
