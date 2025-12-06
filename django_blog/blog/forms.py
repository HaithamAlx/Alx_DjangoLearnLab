from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post
from taggit.forms import TagWidget  # <-- make sure taggit is installed


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class ProfileUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # include tags
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter post title'}),
            'content': forms.Textarea(attrs={'placeholder': 'Write your content here...'}),
            'tags': TagWidget(attrs={'placeholder': 'Add tags separated by commas'}),  # <-- TagWidget
        }
