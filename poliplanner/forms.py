from django import forms
from .models import  Curso, Gerente, Professor, Oferecimento, Subject, Aluno, Tarefa, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ('title', 'author', 'subject' , 'content', 'deadline')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}), 
            'author': forms.Select(attrs={'class': 'form-control'}),
            'subject': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}), 
            'deadline': forms.TextInput(attrs={'class': 'form-control'}), 
        }

        category = forms.ModelMultipleChoiceField(
            queryset = Subject.objects.all(),
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
    