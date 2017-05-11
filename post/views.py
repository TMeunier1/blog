# -*- codipost/ng: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Post


# Create your views here.
def homepage(request):
    return render(request, "homepage.html")

def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, "post_list.html", context)

def post_detail(request, post_slug):
    post = Post.objects.get(slug=post_slug)
    context = {
        'post': post
    }
    return render(request, "post_detail.html", context)
