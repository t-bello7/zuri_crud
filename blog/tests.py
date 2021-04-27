from django.test import TestCase
from .models import Post
from djang.urls import reverse

# Create your tests here.

class BlogTests(TestCase):
    def setUp(self):
        pass

    def test_post_detail_view(self):
        pass