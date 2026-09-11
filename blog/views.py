from .models import Post, Favoritepost
from django.views.generic import ListView
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


class PostList(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    ordering = ['id']
    paginate_by = 6


@login_required
def add_favorite(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if Favoritepost.objects.filter(user=request.user, post=post).exists():
        messages.info(request, "This post is already in your favorites.")
    else:
        Favoritepost.objects.create(user=request.user, post=post)
        messages.success(request, "Added to favorites.")
    return redirect("blog:post_detail", post_id)


class FavoriteList(ListView):
    template_name = 'post_favorite.html'
    context_object_name = 'favorites'
    paginate_by = 6

    def get_queryset(self):
        # Anonymous users get an empty list; the template asks them to log in.
        if not self.request.user.is_authenticated:
            return Favoritepost.objects.none()
        return Favoritepost.objects.filter(user=self.request.user).select_related('post').order_by('id')


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})
