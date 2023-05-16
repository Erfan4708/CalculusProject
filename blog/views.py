from .models import Post
from django.views.generic import ListView, DetailView
from django.db import models


class PostList(ListView):
    model = Post
    template_name = '../templates/post_list.html'
    image = models.ImageField(upload_to='images/')
    context_object_name = "posts"


class PostDetail(DetailView):
    model = Post
    template_name = '../templates/post_detail.html'
    image = models.ImageField(upload_to='detailImages/')
    context_object_name = "post"
