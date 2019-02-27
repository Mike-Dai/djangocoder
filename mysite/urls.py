from django.conf.urls import include, url
from django.contrib import admin

from django.contrib.auth import views as auth_view
#from django_registration.backends.one_step import RegistrationView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
#   url(r'^accounts/register/', RegistrationView.as_view(), name='django_registration_register'),
#   url(r'^accounts/', include('django_registration.backends.one_step.urls')),
#   url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/login/', auth_view.LoginView.as_view(), name='login'),
    url(r'^accounts/logout/', auth_view.LogoutView.as_view(next_page='/'), name='logout'),
    url(r'', include('blog.urls')),
    #url(r'^search/', include('haystack.urls')),
]
