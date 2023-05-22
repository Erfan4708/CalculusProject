
from django.db import models
# from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import get_user_model
User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    information_text = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    favorite = models.BooleanField(default=False)
    # users_like = models.ManyToManyField(User , related_name="users_like")
    html_content = models.TextField(blank=True)
    html_content_grad = models.TextField(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.pk})



class Favoritepost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} -> {self.post.title}"
# python manage.py makemigrations
# python manage.py migrate