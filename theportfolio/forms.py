from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'content', 'post_date')

        widget = {
            'title': form.TextInput(attrs={'class': 'form-control'}), 
            'author': form.TextInput(attrs={'class': 'form-control'}), 
            'content': form.TextInput(attrs={'class': 'form-control'}), 
            'post_date': form.TextInput(attrs={'class': 'form-control'}), 
        }

    