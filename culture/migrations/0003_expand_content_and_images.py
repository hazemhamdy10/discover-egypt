from django.db import migrations, models


IMAGE_URLS = {
    "article-nubian": "https://images.unsplash.com/photo-1568322445389-f64ac2515020?auto=format&fit=crop&w=1200&q=85",
    "article-food": "https://images.unsplash.com/photo-1547592180-85f173990554?auto=format&fit=crop&w=1200&q=85",
    "article-music": "https://images.unsplash.com/photo-1524368535928-5b5e00ddc76b?auto=format&fit=crop&w=1200&q=85",
    "article-festivals": "https://images.unsplash.com/photo-1533929736458-ca588d08c8be?auto=format&fit=crop&w=1200&q=85",
    "article-cotton": "https://images.unsplash.com/photo-1610701596007-11502861dcfa?auto=format&fit=crop&w=1200&q=85",
    "destination-muizz": "https://images.unsplash.com/photo-1568322445389-f64ac2515020?auto=format&fit=crop&w=1200&q=85",
    "destination-qurna": "https://images.unsplash.com/photo-1568322445389-f64ac2515020?auto=format&fit=crop&w=1200&q=85",
    "destination-alexandria": "https://images.unsplash.com/photo-1539650116574-75c0c6d73f6e?auto=format&fit=crop&w=1200&q=85",
    "destination-fayoum": "https://images.unsplash.com/photo-1539650116574-75c0c6d73f6e?auto=format&fit=crop&w=1200&q=85",
    "destination-siwa": "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=1200&q=85",
    "craft-pottery": "https://images.unsplash.com/photo-1610701596007-11502861dcfa?auto=format&fit=crop&w=1200&q=85",
    "craft-textile": "https://images.unsplash.com/photo-1590736969955-71cc94901144?auto=format&fit=crop&w=1200&q=85",
    "craft-jewelry": "https://images.unsplash.com/photo-1617038220319-276d3cfab638?auto=format&fit=crop&w=1200&q=85",
    "craft-wood": "https://images.unsplash.com/photo-1544967082-d9d25d867d66?auto=format&fit=crop&w=1200&q=85",
    "craft-glass": "https://images.unsplash.com/photo-1577083552431-6e5fd01988f5?auto=format&fit=crop&w=1200&q=85",
}


def expand_content(apps, schema_editor):
    Article = apps.get_model("culture", "Article")
    Destination = apps.get_model("culture", "Destination")
    Craft = apps.get_model("culture", "Craft")

    Article.objects.filter(slug="nubian-art").update(image_url=IMAGE_URLS["article-nubian"])
    Article.objects.filter(slug="egyptian-cuisine").update(image_url=IMAGE_URLS["article-food"])
    Article.objects.create(
        title="الموسيقى المصرية بين الماضي والحاضر", slug="egyptian-music",
        category="music", summary="إيقاعات تجمع بين الذكرى والاحتفال وتمنح كل مناسبة صوتها الخاص.",
        content="من التخت الشرقي إلى موسيقى الشارع الحديثة، تعكس الموسيقى المصرية تنوع المجتمع وقدرته على إعادة ابتكار تراثه. لكل مدينة إيقاعها ولكل مناسبة أغنيتها.", status="published", image_url=IMAGE_URLS["article-music"])
    Article.objects.create(
        title="الأعياد والمناسبات في مصر", slug="egyptian-festivals",
        category="traditions", summary="مواسم للفرح والزيارة والطعام تتوارثها العائلات المصرية.",
        content="تمنح المناسبات الشعبية للحارات والقرى طابعًا خاصًا. يشارك الجميع في إعداد الطعام وتزيين الشوارع وتبادل الزيارات، فتتحول الذكرى إلى تجربة جماعية.", status="published", image_url=IMAGE_URLS["article-festivals"])
    Article.objects.create(
        title="القطن المصري: من الحقل إلى النسيج", slug="egyptian-cotton",
        category="identity", summary="رحلة خامة شهيرة تكشف صبر المزارع ومهارة الحرفي.",
        content="ارتبط القطن المصري بجودة الألياف ونعومتها، ثم تحول عبر الغزل والنسيج إلى منسوجات تحمل قيمة اقتصادية وثقافية. ما زالت الحرفة تجمع بين المعرفة القديمة والتقنيات الحديثة.", status="published", image_url=IMAGE_URLS["article-cotton"])

    Destination.objects.filter(slug="al-muizz-street").update(image_url=IMAGE_URLS["destination-muizz"])
    Destination.objects.filter(slug="qurna-luxor").update(image_url=IMAGE_URLS["destination-qurna"])
    Destination.objects.create(
        name="مكتبة الإسكندرية والكورنيش", slug="alexandria-corniche", governorate="الإسكندرية",
        description="مدينة متوسطية تجمع البحر والعمارة والكتب في تجربة ثقافية مفتوحة.",
        cultural_significance="تحافظ الإسكندرية على ذاكرة كوزموبوليتانية تظهر في مبانيها ومتاحفها ومقاهيها.",
        location_details="تقع المكتبة على الكورنيش بالقرب من منطقة الشاطبي.", best_time_to_visit="من سبتمبر إلى مايو.", image_url=IMAGE_URLS["destination-alexandria"])
    Destination.objects.create(
        name="وادي الحيتان", slug="wadi-al-hitan", governorate="الفيوم",
        description="محمية طبيعية تعرض حفريات حيتان قديمة وسط مشهد صحراوي هادئ.",
        cultural_significance="تروي الحفريات قصة تطور الحياة وتربط العلم بالسياحة البيئية في مصر.",
        location_details="داخل محمية وادي الريان، ويُنصح بالتنسيق مع دليل محلي.", best_time_to_visit="من أكتوبر إلى أبريل.", image_url=IMAGE_URLS["destination-fayoum"])
    Destination.objects.create(
        name="واحة سيوة", slug="siwa-oasis", governorate="مطروح",
        description="واحة فريدة تشتهر بالعيون الطبيعية والعمارة الطينية والمناظر الصحراوية.",
        cultural_significance="تحتفظ سيوة بعادات ولهجة وحرف مميزة تشكل جزءًا مهمًا من تنوع الثقافة المصرية.",
        location_details="تقع في الصحراء الغربية بالقرب من الحدود الليبية.", best_time_to_visit="من أكتوبر إلى مارس.", image_url=IMAGE_URLS["destination-siwa"])

    Craft.objects.filter(slug="egyptian-pottery").update(image_url=IMAGE_URLS["craft-pottery"])
    Craft.objects.filter(slug="handwoven-textiles").update(image_url=IMAGE_URLS["craft-textile"])
    Craft.objects.create(
        name="الحلي والمجوهرات", slug="egyptian-jewelry", category="jewelry", origin="القاهرة وأسوان",
        description="قطع صغيرة تحمل رموزًا مستوحاة من النيل والبيئة والذاكرة الشعبية.",
        materials="الفضة والنحاس والأحجار الطبيعية والخرز.", production_process="تُقص المعادن وتُطرق وتُنقش ثم تُجمع مع الأحجار أو الخرز.",
        artisan_information="يمزج الصاغ بين التصميم المعاصر والزخارف المصرية المتوارثة.", image_url=IMAGE_URLS["craft-jewelry"])
    Craft.objects.create(
        name="الأعمال الخشبية", slug="egyptian-woodwork", category="wood", origin="دمياط والقاهرة",
        description="حرفة دقيقة تحول الخشب إلى أثاث وصناديق ومشربيات مزينة.",
        materials="خشب الجوز والزان والأرو، مع الصدف أو النحاس.", production_process="يُقطع الخشب ويُشكل ثم تُضاف الزخارف والتطعيمات ويُصقل السطح.",
        artisan_information="تعتمد الورش العائلية على التدريب الطويل والصبر في تنفيذ التفاصيل.", image_url=IMAGE_URLS["craft-wood"])
    Craft.objects.create(
        name="الزجاج المعشق", slug="stained-glass", category="glass", origin="القاهرة التاريخية",
        description="ألوان من الضوء تتشكل في نوافذ وفوانيس وقطع فنية مستوحاة من العمارة الإسلامية.",
        materials="ألواح زجاجية ملونة، رصاص، وأطر خشبية أو معدنية.", production_process="يُرسم التصميم ثم يُقص الزجاج ويُركب بدقة قبل تثبيته في إطاره.",
        artisan_information="تحافظ الورش المتخصصة على تقنيات تحتاج إلى خبرة عالية وحس فني.", image_url=IMAGE_URLS["craft-glass"])


class Migration(migrations.Migration):
    dependencies = [("culture", "0002_seed_arabic_content")]
    operations = [
        migrations.AddField(model_name="article", name="image_url", field=models.URLField(blank=True)),
        migrations.AddField(model_name="destination", name="image_url", field=models.URLField(blank=True)),
        migrations.AddField(model_name="craft", name="image_url", field=models.URLField(blank=True)),
        migrations.RunPython(expand_content, migrations.RunPython.noop),
    ]
