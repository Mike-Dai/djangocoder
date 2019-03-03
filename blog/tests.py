from django.test import TestCase, Client
from django.http import HttpRequest
from django.urls import resolve, reverse
from django.utils import timezone

from blog.views import IndexView, PostDetailView, post_new, post_edit,\
post_draft_list, search, register
from blog.models import Post, Tag

client = Client()

class HomePageTest(TestCase):
	"""
	def test_root_url_resolvers_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, IndexView)
	
	def test_blog_url_resolvers_to_blog_post_detail(self):
		found = resolve('/post/1/')
		self.assertEqual(found.func, PostDetailView)
"""
	def test_blog_url_resolvers_to_blog_post_new(self):
		found = resolve('/post/new/')
		self.assertEqual(found.func, post_new)

	def test_blog_url_resolvers_to_blog_post_draft_list(self):
		found = resolve('/post/draft/')
		self.assertEqual(found.func, post_draft_list)

	def test_blog_url_resolvers_to_search(self):
		found = resolve('/search/')
		self.assertEqual(found.func, search)

	def test_blog_url_resolvers_to_register(self):
		found = resolve('/register/')
		self.assertEqual(found.func, register)

	def test_post_list_status_code(self):
		response = client.get(reverse('post_list'))
		self.assertEqual(response.status_code, 200)

	def test_post_new_status_code(self):
		response = client.get(reverse('post_new'))
		self.assertEqual(response.status_code, 302)

	def test_login_status_code(self):
		response = client.get(reverse('login'))
		self.assertEqual(response.status_code, 200)

	def test_tags_detail_status_code(self):
		tag = Tag(name='test')
		tag.save()
		response = client.get(tag.get_absolute_url())
		self.assertEqual(response.status_code, 200)
"""
	def test_post_create_with_view(self):
		post = Post(title='test', text='This is a test', created_date=timezone.now(), published_date=timezone.now())
		post.save()
		response = self.client.get(post.get_absolute_url())
		self.assertIn(b'This is a test', response.content)

	def test_blog_url_resolvers_to_blog_post_edit(self):
		found = resolve('/post/edit/')
		self.assertEqual(found.func, post_edit)

	def test_post_create_with_view(self):
		Post.objects.create(title='test', author=request.user, text='This is a test', created_date=timezone.now(), published_date=timezone.now())
		response = self.client.get('/post/7/')
		self.assertIn(b'This is a test', response.content)

	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = post_list(request)
		self.assertIn(b'<title>djangocoder</title>', response.content)
"""