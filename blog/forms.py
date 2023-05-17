from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('favorite',)


class FavoriteForm(forms.Form):
    favorite = forms.BooleanField(required=False)
