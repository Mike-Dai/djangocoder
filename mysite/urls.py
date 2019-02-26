from django.conf.urls import include, url
from django.contrib import admin

from django.contrib.auth import views as auth_view

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', admin.site.urls),
    #url(r'^accounts/login/', auth_view.LoginView.as_view(template_name=template_name), name='login'),
    #url(r'^accounts/logout/', auth_view.LogoutView.as_view(next_page='/'), name='logout'),
    url(r'', include('blog.urls')),
    #url(r'^search/', include('haystack.urls')),
]
