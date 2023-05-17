from .models import Post
from django.views.generic import ListView, DetailView
from django.db import models
from django.shortcuts import get_object_or_404 ,render
from .forms import PostForm , FavoriteForm
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin


class PostList(ListView):
    model = Post
    template_name = '../templates/post_list.html'
    # image = models.ImageField(upload_to='images/')
    context_object_name = "posts"
    paginate_by = 6

class FavoriteList(LoginRequiredMixin,ListView):
    model = Post
    template_name = '../templates/post_favorite.html'
    image = models.ImageField(upload_to='images/')
    context_object_name = "post_f"
    paginate_by = 6
    # def test_func(self):
    #     obj = self.get_object()
    #     return obj.user == self.request.user
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = FavoriteForm(initial={'favorite': post.favorite})
    if request.method == 'POST':
        form = FavoriteForm(request.POST)
        if form.is_valid():
            post.favorite = form.cleaned_data['favorite']
            post.save()
    return render(request, '../templates/post_detail.html', {'post': post, 'form': form})

