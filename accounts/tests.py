from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class SignUpTests(TestCase):
    def test_signup_creates_user_and_redirects_to_login(self):
        response = self.client.post(reverse('signup'), {
            'username': 'carol',
            'password1': 'a-strong-pass-987',
            'password2': 'a-strong-pass-987',
        })
        self.assertRedirects(response, reverse('login'))
        self.assertTrue(get_user_model().objects.filter(username='carol').exists())

    def test_logout_redirects_to_post_list(self):
        get_user_model().objects.create_user('dave', password='test-pass-123')
        self.client.login(username='dave', password='test-pass-123')
        response = self.client.post(reverse('logout'))
        self.assertRedirects(response, reverse('blog:post_list'))
