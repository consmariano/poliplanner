from django import forms
from .models import Post, Comment, Category

# choices = Category.objects.all().values_list('name','name')

# choice_list = []
# for item in choices:
#     choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'category' , 'content', 'post_date')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}), 
            'author': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}), 
            'post_date': forms.TextInput(attrs={'class': 'form-control'}), 
        }

        category = forms.ModelMultipleChoiceField(
            queryset = Category.objects.all(),
            widget=forms.CheckboxSelectMultiple
        )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('username','content')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}), 
            'content': forms.Textarea(attrs={'class': 'form-control'}), 
        }
    