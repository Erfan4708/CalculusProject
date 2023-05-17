from .models import Post
from django.views.generic import ListView, DetailView
from django.db import models
from django.shortcuts import get_object_or_404 ,render
from .forms import PostForm , FavoriteForm


class PostList(ListView):
    model = Post
    template_name = '../templates/post_list.html'
    image = models.ImageField(upload_to='images/')
    context_object_name = "posts"
    paginate_by = 6

class FavoriteList(ListView):
    model = Post
    template_name = '../templates/post_favorite.html'
    image = models.ImageField(upload_to='images/')
    context_object_name = "post_f"
    paginate_by = 6
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = FavoriteForm(initial={'favorite': post.favorite})
    if request.method == 'POST':
        form = FavoriteForm(request.POST)
        if form.is_valid():
            post.favorite = form.cleaned_data['favorite']
            post.save()
    return render(request, '../templates/post_detail.html', {'post': post, 'form': form})

