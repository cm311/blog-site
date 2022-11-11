from django.forms import ModelForm
from django import forms
from .models import *

class ArticleForm(forms.Form):
    title = forms.CharField(strip=False, label='Article Title')
    body = forms.CharField(widget=forms.Textarea, strip=False, label='Article body')

    class Meta:
        model = Article

class LoginForm(forms.Form):
    username = forms.CharField(strip=False, label='UserName')
    password = forms.CharField(widget=forms.PasswordInput(), label='Password')

class CommentForm(forms.Form):

    body = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Comment
