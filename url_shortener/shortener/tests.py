from django.test import TestCase
from .models import ShortURL
from .views import *


class UrlTestCase(TestCase):

    def setUp(self, url='url = "http://www.example.com"', unique_id=get_unique_string()):
        return ShortURL.objects.create(url=url, unique_id=get_unique_string())

    def test_setUp(self):
        w = self.setUp()
        self.assertTrue(isinstance(w, ShortURL))
        self.assertEqual(w.__unicode__(), w.url)

    def test_short_url_large(self):
        url = "http://www.example.com"
        unique_id = get_unique_string()
        short_url = settings.SITE_URL + "/" + unique_id
        self.assertLess(len(short_url), len(url))

    def test_short_code_duplication(self):
        url = "http://www.example.com"
        uid = get_unique_string()
        u = ShortURL(url=url)
        self.assertEqual(u.short_id, uid)