from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'content', 'post_date')

        widget = {
            'title': forms.TextInput(attrs={'class': 'form-control'}), 
            'author': forms.TextInput(attrs={'class': 'form-control'}), 
            'content': forms.Select(attrs={'class': 'form-control'}), 
            'post_date': forms.TextInput(attrs={'class': 'form-control'}), 
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('username','content')

        widget = {
            'username': forms.TextInput(attrs={'class': 'form-control'}), 
            'content': forms.Textarea(attrs={'class': 'form-control'}), 
        }
    