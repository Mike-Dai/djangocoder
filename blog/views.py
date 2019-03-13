import markdown

from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.utils import timezone
from .models import Post, Comment, Tag
from django.contrib.auth.models import User
from .forms import PostForm, CommentForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import Http404
from django.contrib.admin.views.decorators import staff_member_required

class IndexView(ListView):
	model = Post
	template_name = 'blog/home.html'
	context_object_name = 'posts'
	paginate_by = 2

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		paginator = context.get('paginator')
		page = context.get('page_obj')
		is_paginated = context.get('is_paginated')
		pagination_data = self.pagination_data(paginator, page, is_paginated)
		context.update(pagination_data)
		return context

	def pagination_data(self, paginator, page, is_paginated):
		if not is_paginated:
			return {}
		left = []
		right = []
		left_has_more = False
		right_has_more = False
		first = False
		last = False
		page_number = page.number
		total_pages = paginator.num_pages
		page_range = paginator.page_range
		if page_number == 1:
			right = page_range[page_number:page_number +2]
			if right[-1] < total_pages - 1:
				right_has_more = True
			if right[-1] < total_pages:
				last = True
		elif page_number == total_pages:
			left = page_range[(page_number - 3) if (page_number - 3) > 0 else 0: page_number - 1]
			if left[0] > 2:
				left_has_more = True
			if left[0] > 1:
				first = True
		else:
			left = page_range[(page_number - 3) if (page_number - 3) > 0 else 0:page_number - 1]
			right = page_range[page_number:page_number + 2]
			if right[-1] < total_pages - 1:
				right_has_more = True
			if right[-1] < total_pages:
				last = True
			if left[0] > 2:
				left_has_more = True
			if left[0] > 1:
				first = True
		data = {
			'left': left,
			'right': right,
			'left_has_more': left_has_more,
			'right_has_more': right_has_more,
			'first': first,
			'last': last,
			'page_range': page_range,
		}
		return data
"""
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
"""

class PostDetailView(DetailView):
	model = Post
	template_name = 'blog/post_detail.html'
	context_object_name = 'post'

	def get(self, request, *args, **kwargs):
		response = super(PostDetailView, self).get(request, *args, **kwargs)
		self.object.increase_views()
		return response

	def get_object(self, queryset=None):
		post = super(PostDetailView, self).get_object(queryset=None)
		post.text = markdown.markdown(post.text,
									extensions=[
										'markdown.extensions.extra',
	                                    'markdown.extensions.codehilite',
	                                    'markdown.extensions.toc',
	                                    ])
		return post

def previous_post(request, pk):
	post = get_object_or_404(Post, pk=pk)
	prev_post = post.filter(pk__lt=post.pk)[0:1]
	return render(request, 'blog/post_detail', {'prev_post':prev_post})

def next_post(request, pk):
	post = get_object_or_404(Post, pk=pk)
	next_post = post.filter(pk__gt=post.pk)[0:1]
	return render(request, 'blog/post_detail', {'next_post':next_post})

@login_required
def post_new(request):
	if request.user.is_staff or request.user.is_superuser:
		if request.method == 'POST':
			form = PostForm(request.POST)
			if form.is_valid():
				post = form.save(commit=False)
				post.author = request.user
				#post.published_date = timezone.now()
				post.save()
				return redirect('post_detail', pk=post.pk)
		else:
			form = PostForm()
	else:
		raise Http404
	return render(request, 'blog/post_new.html',{'form': form})

@login_required
def post_edit(request, pk):
	if request.user.is_staff or request.user.is_superuser:
		post = get_object_or_404(Post, pk=pk)
		if request.method == "POST":
			form = PostForm(request.POST, instance=post)
			if form.is_valid():
				post = form.save(commit=False)
				post.author = request.user
				#post.published_date = timezone.now()
				post.save()
				return redirect('post_detail', pk=post.pk)
		else:
			form = PostForm(instance=post)
	else:
		raise Http404
	return render(request, 'blog/post_edit.html',{'form': form})

@staff_member_required
def post_draft_list(request):
	posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
	return render(request, 'blog/post_list.html', {'posts': posts})

@staff_member_required
def post_publish(request, pk):
	post = get_object_or_404(Post,pk=pk)
	post.published_date = timezone.now()
	post.save()
	return redirect('post_detail', pk=post.pk)

@staff_member_required
def post_delete(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.delete()
	redirect('post_list')

@login_required
def add_comment(request, pk):
	post = Post.objects.get(pk=pk)
	if request.method == "POST":
		form = CommentForm(request.POST)
		#return HttpResponse(form.errors)
		#print(form.errors)
		if form.is_valid():
			#return HttpResponse(form.is_valid())
			comment = form.save(commit=False)
			comment.author = request.user
			comment.created_date = timezone.now()
			comment.post = post
			#comment.text = form.text
			#comment.approve()
			comment.save()
			return redirect('post_detail', pk=post.pk)
	else:
		#return HttpResponse(request.method)
		form = CommentForm()
	return render(request, 'blog/add_comment.html', {'form': form})

@staff_member_required
def approve_comment(request,pk):
	comment = get_object_or_404(Comment, pk=pk)
	post = comment.post
	comment.approve()
	return redirect('post_detail',pk=post.pk)

@staff_member_required
def remove_comment(request,pk):
	comment = get_object_or_404(Comment, pk=pk)
	post = comment.post
	comment.delete()
	return redirect('post_detail',pk=post.pk)

class ArchivesView(ListView):
	model = Post
	template_name = 'blog/post_list.html'
	context_object_name = 'posts'
	paginate_by = 2;

	def get_queryset(self):
		year = self.kwargs.get('year')
		month = self.kwargs.get('month')
		return super(ArchivesView, self).get_queryset().filter(created_date__year=year,
									created_date__month=month,
									).order_by('-created_date')
"""
def archives(request, year, month):
	post_list = Post.objects.filter(created_date__year=year,
									created_date__month=month,
									).order_by('-created_date')
	return render(request, 'blog/post_list.html', {'posts':post_list})
"""
class TagsView(ListView):
	model = Post
	template_name = 'blog/post_list.html'
	context_object_name = 'posts'
	paginate_by = 2

	def get_queryset(self):
		tag = get_object_or_404(Tag, pk=self.kwargs.get('pk'))
		return super(TagsView, self).get_queryset().filter(tags__name=tag.name).order_by('-created_date')
"""
def tag_detail(request, pk):
	tag = get_object_or_404(Tag, pk=pk)
	post_list = Post.objects.filter(tags__name=tag.name)
	return render(request, 'blog/post_list.html', {'posts':post_list})
"""
def search(request):
	q = request.GET.get('q')
	error_msg = ''

	if not q:
		error_msg = "Please enter the key word"
		return render(request, 'blog/post_list.html', {'error_msg':error_msg})
	posts = Post.objects.filter(Q(title__icontains=q) | Q(text__icontains=q))
	return render(request, 'blog/post_list.html', {'error_msg':error_msg, 'posts':posts})

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			#new_user.groups.add(guest)
			return redirect('login')
	else:
		form = UserCreationForm()
	return render(request, 'registration/registration_form.html', {'form': form})

@login_required
def user_profile(request):
	user = request.user
	return render(request, 'blog/user_profile.html', {'user': user})

@login_required
def profile_edit(request):
	user = request.user
	if request.method == "POST":
		form = ProfileForm(request.POST, instance=user)
		if form.is_valid():
			user = form.save(commit=False)
			user.save()
			return redirect('user_profile')
	else:
		form = ProfileForm(instance=user)
	return render(request, 'blog/profile_edit.html', {'form': form})
