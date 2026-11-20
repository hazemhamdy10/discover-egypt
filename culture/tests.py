from django.test import TestCase
from django.urls import reverse

from .models import Article, Craft, Destination


class PublicPagesTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.article = Article.objects.create(
            title="مقال تجريبي",
            slug="test-article",
            category="arts",
            summary="ملخص",
            content="محتوى المقال",
            status="published",
        )
        cls.destination = Destination.objects.create(
            name="وجهة تجريبية",
            slug="test-destination",
            governorate="القاهرة",
            description="وصف الوجهة",
        )
        cls.craft = Craft.objects.create(
            name="حرفة تجريبية",
            slug="test-craft",
            category="pottery",
            origin="القاهرة",
            description="وصف الحرفة",
        )

    def test_main_pages_render_in_arabic_layout(self):
        urls = [
            reverse("culture:home"),
            reverse("culture:articles"),
            reverse("culture:destinations"),
            reverse("culture:crafts"),
        ]
        for url in urls:
            response = self.client.get(url, secure=True)
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, 'lang="ar"')
            self.assertContains(response, 'dir="rtl"')

    def test_detail_pages_render(self):
        urls = [
            reverse("culture:article_detail", args=[self.article.slug]),
            reverse("culture:destination_detail", args=[self.destination.slug]),
            reverse("culture:craft_detail", args=[self.craft.slug]),
        ]
        for url in urls:
            self.assertEqual(self.client.get(url, secure=True).status_code, 200)

    def test_topic_images_are_unique(self):
        image_urls = []
        for model in (Article, Destination, Craft):
            image_urls.extend(
                value for value in model.objects.values_list("image_url", flat=True)
                if value
            )
        self.assertEqual(len(image_urls), len(set(image_urls)))
