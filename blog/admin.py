from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Post, Comment, Tag, Profile
from django.contrib.auth.models import User

class PostAdmin(admin.ModelAdmin):
	filter_horizontal = ('tags',)

class ProfileInline(admin.StackedInline):
	model = Profile
	can_delete = False
	verbose_name_plural = 'profile'

class UserAdmin(BaseUserAdmin):
	inline = (ProfileInline,)

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Tag)
#admin.site.unregister(User)
#admin.site.register(User,UserAdmin)