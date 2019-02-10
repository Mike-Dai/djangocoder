from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify

class Post(models.Model):
	title = models.CharField(max_length=200)
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	category = models.ForeignKey('blog.Category', on_delete=models.CASCADE)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

class Category(models.Model):
	name = models.CharField(max_length=200)
	number = models.IntegerField(default=0)

	def __str__(self):
		return self.name
	#slug = models.SlugField(default='')
"""
	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)
"""
    

	