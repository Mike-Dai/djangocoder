from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Comment, Category
from .forms import PostForm, CommentForm, CategoryForm
from django.contrib.auth.decorators import login_required


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    categories = Category.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts,'categories':categories})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	"""
	views = request.session.get('views')
	if not views:
		views = 1
	else:
		views = views + 1
	"""
	views = post.views
	views = views + 1
	post.views = views
	post.save()
	return render(request, 'blog/post_detail.html', {'post':post,'views':views})

@login_required
def post_new(request):
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
	return render(request, 'blog/post_new.html',{'form': form})

@login_required
def post_edit(request, pk):
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
	return render(request, 'blog/post_edit.html',{'form': form})

@login_required
def post_draft_list(request):
	posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
	return render(request, 'blog/post_draft_list.html', {'posts': posts})

@login_required
def post_publish(request, pk):
	post = get_object_or_404(Post,pk=pk)
	post.published_date = timezone.now()
	post.save()
	return redirect('post_detail', pk=post.pk)

@login_required
def post_delete(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.delete()
	redirect('post_list')

@login_required
def add_comment(request, pk):
	post = Post.objects.get(pk=pk)
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.created_date = timezone.now()
			comment.post = post
			comment.save()
			return redirect('post_detail', pk=pk)
	else:
		form = CommentForm()
	return render(request, 'blog/add_comment.html', {'form': form})

@login_required
def approve_comment(request,pk):
	comment = get_object_or_404(pk=pk)
	post = comment.post
	comment.publish()
	return redirect('post_detail',pk=post.pk)

@login_required
def remove_comment(request,pk):
	comment = get_object_or_404(pk=pk)
	post = comment.post
	comment.delete()
	return redirect('post_detail',pk=post.pk)

def add_category(request):
	if request.method == "POST":
		form = CategoryForm(request.POST)
		if form.is_valid():
			category = form.save(commit=False)
			category.save()
			return redirect('post_list')
	else:
		form = CategoryForm()
	return render(request, 'blog/add_category.html', {'form':form})
