from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')


def post_list(request):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', {'post_list' : post_list})


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'post' : post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect(post_detail, post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form' : form})


def post_edit(request, pk):
    post = Post.objects.get(pk=pk)
    if request.mehtod == "POST":
        form = PostForm(request.FILES, request.POST, instance=post)
        if form.is_valid:
            post = form.save()
            return redirect('blog/post_detail.html', post.pk)

    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form', form})