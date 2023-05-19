from django import forms
from .models import Post ,Favoritepost


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('favorite',)


# class FavoriteForm(forms.Form):
#     favorite = forms.BooleanField(required=False)

# from django import forms

# class AddToFavoritesForm(forms.Form):
#     book_id = forms.IntegerField(widget=forms.HiddenInput)