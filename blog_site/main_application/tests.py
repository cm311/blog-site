from django.test import TestCase
from .models import *

# Create your tests here.
class TestArticle(TestCase):
    def setUp(self):
        is_creatable = Article.objects.create(article_title='Test', body='Test')

    def tearDown(self):
        pass

    def test_is_creatable(self):
        self.assertNotEqual(type(is_creatable), None)



