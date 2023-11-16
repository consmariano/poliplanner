from django.shortcuts import render
from .models import Post

def home(request):
    return render(request, 'home.html', {})

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})
