from django.conf.urls import include, url
from django.contrib.auth.models import User
from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from django.contrib.auth import views as auth_view
from blog.models import Post, Tag, Comment
from rest_framework_swagger.views import get_swagger_view
#from django_registration.backends.one_step import RegistrationView

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'is_staff')

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class PostSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Post
		fields = ('title', 'author', 'text', 'created_date', 'published_date', 'views')

class PostViewSet(viewsets.ModelViewSet):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

class TagSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Tag
		fields = ('name',)

class TagViewSet(viewsets.ModelViewSet):
	queryset = Tag.objects.all()
	serializer_class = TagSerializer

class CommentSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Comment
		fields = ('post', 'author', 'text', 'created_date')

class CommentViewSet(viewsets.ModelViewSet):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'post', PostViewSet)
router.register(r'tag', TagViewSet)
router.register(r'comment', CommentViewSet)

schema_view = get_swagger_view(title='djangocoder API')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
#   url(r'^accounts/register/', RegistrationView.as_view(), name='django_registration_register'),
#   url(r'^accounts/', include('django_registration.backends.one_step.urls')),
#   url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/login/', auth_view.LoginView.as_view(), name='login'),
    url(r'^accounts/logout/', auth_view.LogoutView.as_view(next_page='/'), name='logout'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'', include('blog.urls')),
    url(r'^schema/', schema_view),
    #url(r'^search/', include('haystack.urls')),
]
