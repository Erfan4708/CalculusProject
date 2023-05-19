from .models import Post ,Favoritepost
from django.views.generic import ListView , DeleteView
from django.shortcuts import get_object_or_404, render , redirect
from django.urls import reverse_lazy
from django.contrib import messages


class PostList(ListView):
    model = Post
    template_name = '../templates/post_list.html'
    context_object_name = "posts"
    paginate_by = 6
def add_favorite(request,user,post_id):
    post = get_object_or_404(Post, pk=post_id)
    Favoritepost.objects.create(user=request.user, post=post)
    post_favorite = Favoritepost.objects.filter(user=request.user, post=post)
    messages.success(request, "Added to favorites.")
    return redirect("blog:post_detail",post_id)


# def remove_favorite(request, post_id):
#     post = get_object_or_404(Post, pk=post_id)
#     favorite_post = Favoritepost.objects.filter(user=request.user, post=post)
#     if favorite_post.exists():
#         favorite_post.delete()
#         messages.success(request, "Removed from favorites.")
#     else:
#         messages.error(request, "This post was not in your favorites.")
#     return redirect("blog:post_detail", post_id)


class FavoriteList(ListView):
    model = Favoritepost
    template_name = 'post_favorite.html'
    context_object_name = 'post_f'
    paginate_by = 6


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, '../templates/post_detail.html', {'post': post})
