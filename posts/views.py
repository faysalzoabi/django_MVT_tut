from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Post
from .forms import PostForm
# Create your views here.


def list_posts(request):
    posts = Post.objects.all()
    context = {
        'post_list': posts
    }
    return render(request, 'post_list.html', context)


def post_detail(request, id):
    post = Post.objects.get(id=id)
    context = {
        'post': post
    }
    return render(request, 'post_detail.html', context)


def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/posts')
    context = {
        'form': form,
        'form_type': 'Create'
    }
    return render(request, 'post_create.html', context)


def post_update(request, id):
    post = Post.objects.get(id=id)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/posts')
    context = {
        'form': form,
        'form_type': 'Update'
    }
    return render(request, 'post_create.html', context)


def post_delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return HttpResponseRedirect('/posts')
