from ..models import Post, Tag
from django import template

register = template.Library()

@register.simple_tag
def get_recent_posts(num=5):
	return Post.objects.all().order_by('-created_date')[:num]

@register.simple_tag
def archives():
	return Post.objects.dates('created_date','month',order='DESC')

@register.simple_tag
def tags():
	return Tag.objects.all()