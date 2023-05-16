from .models import Post
from django.views.generic import ListView , DetailView

class PostList(ListView):
    model = Post
    template_name = '../templates/post_list.html'
    context_object_name = "posts"


class PostDetail(DetailView):
    model = Post
    template_name = '../templates/post_detail.html'
    context_object_name = "post"

