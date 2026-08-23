# blog/views.py
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post


def home(request):
    latest_posts = Post.objects.all()[:5]
    context = {"latest_posts": latest_posts}
    return render(request, "blog/home.html", context)


def post_list(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 3)

    page_number = request.GET.get("page")
    posts = paginator.get_page(page_number)

    context = {
        "posts": posts,
        "is_paginated": True,
    }
    return render(request, "blog/post_list.html", context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {"post": post}
    return render(request, "blog/post_detail.html", context)
