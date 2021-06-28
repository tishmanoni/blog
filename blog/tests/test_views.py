from django.test import TestCase, Client
from blog.views import postlist
from django.urls import reverse, resolve


class Test_postlist_view(TestCase):


    def setup(self):
        self.client = Client()
        

    def test_view_list(self):
        
        response = self.client.get(reverse("blog:bloglist"))
        self.assertEquals(response.status_code, 200)
         
        self.assertTemplateUsed(response, 'blog/list.html')