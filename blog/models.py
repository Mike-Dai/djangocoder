from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.models import (
	BaseUserManager, AbstractBaseUser
)

class Tag(models.Model):
	name = models.CharField(max_length=100)

	def get_absolute_url(self):
		return reverse('tag_detail', kwargs={'pk':self.pk})

	def __str__(self):
		return self.name

class Post(models.Model):
	title = models.CharField(max_length=200)
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	img_link = models.CharField(default='images/logo.jpeg', max_length=255)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	views = models.PositiveIntegerField(default=0)
	tags = models.ManyToManyField(Tag, blank=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def increase_views(self):
		self.views = self.views + 1
		self.save(update_fields=['views'])

	def get_absolute_url(self):
		return reverse('post_detail', kwargs={'pk':self.pk})

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

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	level = models.PositiveIntegerField(default=0)

class MyUser(AbstractBaseUser):
	age = models.PositiveIntegerField(default=0)