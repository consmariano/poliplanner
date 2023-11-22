from typing import Any
from django import http
from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Curso, Gerente, Professor, Oferecimento, Subject, Aluno, Tarefa, Comment
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import Http404, HttpResponseRedirect
from django.contrib import messages
from .forms import CustomUserForm, CommentForm

def cadastro(request): 
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else: 
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        user = User.objects.filter(username=username).first()

        if user: 
            messages.error(request, 'Já existe um usuário com esse username.')
            return HttpResponseRedirect(reverse('cadastro'))

        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()

        messages.success(request, 'Usuário cadastrado com sucesso.')
        return redirect('home')


def login(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['senha']
            
            user = authenticate(request, username=username, password=password)

            if user:
                login_django(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Email ou senha inválidos.')
    else:
        form = CustomUserForm()

    return render(request, 'login.html', {'form': form})

class HomeView(ListView):
    model = None
    template_name = 'home.html'

    @method_decorator(login_required(login_url="/cadastro"))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get_queryset(self):
        return Tarefa.objects.order_by('-deadline')[:5] #I want to show the latest 5 posts. 

#Post virou tarefa e Category virou Subject

class PostsListView(ListView):
    model = Tarefa
    template_name = 'post_list.html'
    context_object_name = 'posts'

class ListCategoriesView(ListView):
    model = Subject
    template_name = 'list_categories.html'
    context_object_name = 'list_categories'

def CategoryView(request, cats):
    cat = get_object_or_404(Subject, id=cats)
    category_posts = Post.objects.filter(category=cat)

    context = {
        "cat_name": cat.name,
        "category_posts": category_posts,
        "categories": reverse('categories', kwargs={'cats': cat.id}),
    }

    return render(request, "categories.html", context)

class SinglePostDetailView(DetailView):
    model = Tarefa 
    template_name = 'post_single.html'
    context_object_name = 'post_single'

    #Responde com 404 caso seja requisitado um post inexistente.
    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Http404:
            raise Http404("O item solicitado não existe.")

class CreatePostView(CreateView):
    model = Tarefa
    form_class = Tarefa
    template_name = 'create_post.html'
    success_url = reverse_lazy('home')

    #@method_decorator(login_required(login_url="/login"))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class AddCategoryView(CreateView):
    model = Tarefa
    fields = '__all__'
    template_name = 'create_category.html'
    success_url = reverse_lazy('home')

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'create_comment.html' 

    #@method_decorator(login_required(login_url="/login"))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        form.instance.post = post
        return super().form_valid(form)
    
    success_url = reverse_lazy('home')

class EditPostView(UpdateView):
    model = Tarefa
    template_name = 'edit_post.html'
    fields = ['title', 'category', 'content', 'post_date']

    #@method_decorator(login_required(login_url="/login"))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class RemovePostView(DeleteView):
    model = Tarefa
    template_name = 'remove_post.html'
    success_url = reverse_lazy('home')

    @method_decorator(login_required(login_url="/login"))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    #Implementar uma página de confirmação
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['confirmar_exclusao'] = True  # Adiciona uma variável de confirmação ao contexto
        return context