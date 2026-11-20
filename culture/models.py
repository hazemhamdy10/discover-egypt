
from django.db import models
from django.utils import timezone


class Article(models.Model):

    CATEGORY_CHOICES = [
        ('history', 'التاريخ المصري'),
        ('traditions', 'العادات والتقاليد'),
        ('arts', 'الفنون المصرية'),
        ('food', 'المطبخ المصري'),
        ('music', 'الموسيقى'),
        ('identity', 'الهوية المصرية'),
    ]

    STATUS_CHOICES = [
        ('draft', 'مسودة'),
        ('published', 'منشور'),
    ]

    title = models.CharField(max_length=200)

    slug = models.SlugField(unique=True)

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES
    )

    summary = models.TextField(max_length=500)

    content = models.TextField()

    cover_image = models.ImageField(
        upload_to='articles/',
        blank=True,
        null=True
    )

    image_url = models.URLField(blank=True)

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='draft'
    )

    published_at = models.DateTimeField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'مقال'
        verbose_name_plural = 'المقالات'



class Destination(models.Model):

    name = models.CharField(max_length=200)

    slug = models.SlugField(unique=True)

    governorate = models.CharField(max_length=100)

    description = models.TextField()

    cultural_significance = models.TextField(
        blank=True
    )

    location_details = models.CharField(
        max_length=255,
        blank=True
    )

    cover_image = models.ImageField(
        upload_to='destinations/',
        blank=True,
        null=True
    )

    image_url = models.URLField(blank=True)

    best_time_to_visit = models.CharField(
        max_length=150,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'وجهة سياحية'
        verbose_name_plural = 'الوجهات السياحية'



class Craft(models.Model):

    CATEGORY_CHOICES = [
        ('pottery', 'الفخار والخزف'),
        ('textiles', 'النسيج والتطريز'),
        ('jewelry', 'الحلي والمجوهرات'),
        ('wood', 'الأعمال الخشبية'),
        ('glass', 'الزجاج'),
        ('other', 'أخرى'),
    ]

    name = models.CharField(max_length=200)

    slug = models.SlugField(unique=True)

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES
    )

    origin = models.CharField(max_length=150)

    description = models.TextField()

    materials = models.TextField(blank=True)

    production_process = models.TextField(blank=True)

    artisan_information = models.TextField(blank=True)

    cover_image = models.ImageField(
        upload_to='crafts/',
        blank=True,
        null=True
    )

    image_url = models.URLField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'حرفة'
        verbose_name_plural = 'الحرف والصناعات الثقافية'
