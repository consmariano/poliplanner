from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

# def home(request):
#     return render(request, 'home.html', {})

# def post_list(request):
#     posts = Post.objects.all()
#     return render(request, 'post_list.html', {'posts': posts})

# def post_single(request, pk):
#     single_post = get_object_or_404(Post, id= int(pk) )
#     return render(request, 'post_single.html', {'single_post': single_post})

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
    template_name = 'create_post.html'
    fields = '__all__'

class EditPostView(UpdateView):
    model = Post
    template_name = 'edit_post.html'
    fields = ['title', 'content', 'post_date']

class RemovePostView(DeleteView):
    model = Post
    template_name = 'remove_post.html'

    #Implementar uma página de confirmação
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['confirmar_exclusao'] = True  # Adiciona uma variável de confirmação ao contexto
        return context