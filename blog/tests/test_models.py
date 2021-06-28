from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.models import Post

class Test_model_attr(SimpleTestCase):

    def test_model(self):
        self.assertTrue(hasattr(Post, 'title'))

