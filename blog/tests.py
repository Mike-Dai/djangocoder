from django.test import TestCase
from django.http import HttpRequest
from django.core.urlresolvers import resolve
from django.utils import timezone

from blog.views import post_list, post_detail, post_new
from blog.models import Post

class HomePageTest(TestCase):
	def test_root_url_resolvers_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, post_list)
	
	def test_blog_url_resolvers_to_blog_post_detail(self):
		found = resolve('/post/1/')
		self.assertEqual(found.func, post_detail)

	def test_blog_url_resolvers_to_blog_post_new(self):
		found = resolve('/post/new/')
		self.assertEqual(found.func, post_new)
"""
	def test_post_create_with_view(self):
		Post.objects.create(title='test', author=request.user, text='This is a test', created_date=timezone.now(), published_date=timezone.now())
		response = self.client.get('/post/7/')
		self.assertIn(b'This is a test', response.content)

	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = post_list(request)
		self.assertIn(b'<title>djangocoder</title>', response.content)
"""