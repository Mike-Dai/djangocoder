from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^post/draft/$', views.post_draft_list, name='post_draft_list'),
	url(r'^post/(?P<pk>[0-9]+)/publish/$', views.post_publish, name='post_publish'),
	url(r'^post/(?P<pk>[0-9]+)/delete/$', views.post_delete, name='post_delete'),
	url(r'^post/(?P<pk>[0-9]+)/add_comment/$', views.add_comment, name='add_comment'),
	url(r'^comment/(?P<pk>[0-9]+)/approve/$', views.approve_comment, name='approve_comment'),
	url(r'^comment/(?P<pk>[0-9]+)/remove/$', views.remove_comment, name='remove_comment'),
	url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
]

