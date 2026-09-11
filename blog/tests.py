from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Post, Favoritepost

User = get_user_model()


class BlogViewsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('alice', password='test-pass-123')
        self.other_user = User.objects.create_user('bob', password='test-pass-123')
        self.post = Post.objects.create(
            title='Helix',
            image='images/helix.gif',
            information_text='A simple helix.',
            author=self.user,
        )

    def test_post_list_and_detail_pages_load(self):
        response = self.client.get(reverse('blog:post_list'))
        self.assertContains(response, 'Helix')

        response = self.client.get(reverse('blog:post_detail', args=[self.post.pk]))
        self.assertContains(response, 'A simple helix.')

    def test_add_favorite_requires_login(self):
        url = reverse('blog:add_favorite', args=[self.post.pk])
        response = self.client.get(url)
        self.assertRedirects(response, f"{reverse('login')}?next={url}")
        self.assertFalse(Favoritepost.objects.exists())

    def test_add_favorite_does_not_create_duplicates(self):
        self.client.force_login(self.user)
        url = reverse('blog:add_favorite', args=[self.post.pk])
        self.client.get(url)
        self.client.get(url)
        self.assertEqual(Favoritepost.objects.filter(user=self.user, post=self.post).count(), 1)

    def test_favorite_list_only_shows_own_favorites(self):
        other_post = Post.objects.create(
            title='Saddle',
            image='images/saddle.gif',
            information_text='A saddle surface.',
            author=self.user,
        )
        Favoritepost.objects.create(user=self.user, post=self.post)
        Favoritepost.objects.create(user=self.other_user, post=other_post)

        self.client.force_login(self.user)
        response = self.client.get(reverse('blog:favorite_list'))
        self.assertEqual([favorite.post for favorite in response.context['favorites']], [self.post])
