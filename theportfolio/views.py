from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from django.urls import reverse_lazy
from .forms import PostForm, CommentForm


class HomeView(ListView):
    model = None
    template_name = 'home.html'

    def get_queryset(self):
        return Post.objects.order_by('-post_date')[:5] #I want to show the latest 5 posts. 

class PostsListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'

class SinglePostDetailView(DetailView):
    model = Post
    template_name = 'post_single.html'
    context_object_name = 'post_single'

    #Responde com 404 caso seja requisitado um post inexistente.
    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Http404:
            raise Http404("O item solicitado não existe.")

class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'create_post.html'
    success_url = reverse_lazy('home')

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'create_comment.html' 

    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        form.instance.post = post
        return super().form_valid(form)
    
    success_url = reverse_lazy('home')

class EditPostView(UpdateView):
    model = Post
    template_name = 'edit_post.html'
    fields = ['title', 'content', 'post_date']

class RemovePostView(DeleteView):
    model = Post
    template_name = 'remove_post.html'
    success_url = reverse_lazy('home')

    #Implementar uma página de confirmação
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['confirmar_exclusao'] = True  # Adiciona uma variável de confirmação ao contexto
        return context