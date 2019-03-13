from django import forms

from .models import Post, Comment
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'tags', 'img_link', 'text')

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('text',)

class ProfileForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')