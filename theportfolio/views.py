from django.shortcuts import render, get_object_or_404
from .models import Post

def home(request):
    return render(request, 'home.html', {})

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

def post_single(request, pk):
    single_post = get_object_or_404(Post, id= int(pk) )
    return render(request, 'post_single.html', {'single_post': single_post})