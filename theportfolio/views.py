from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post


def home(request):
    latest_posts = Post.objects.order_by('-post_date')[:5]
    return render(request, 'home.html', {'latest_posts': latest_posts})

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

def single_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_single.html', {'post': post})

def create_post(request):
    if request.method == 'POST':
        Post.objects.create(title=request.POST['title'], author=request.POST['author'], content=request.POST['content'])
        return redirect('post_list')

    return render(request, 'create_post.html')

def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.post_date = request.POST['post_date']
        post.save()
        return redirect('post_list')

    return render(request, 'edit_post.html', {'post': post})

def remove_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('home')

    return render(request, 'remove_post.html', {'post': post, 'confirmar_exclusao': True})


# class HomeView(ListView):
#     model = None
#     template_name = 'home.html'

#     def get_queryset(self):
#         return Post.objects.order_by('-post_date')[:5] #I want to show the latest 5 posts. 

# class PostsListView(ListView):
#     model = Post
#     template_name = 'post_list.html'
#     context_object_name = 'posts'

# class SinglePostDetailView(DetailView):
#     model = Post
#     template_name = 'post_single.html'
#     context_object_name = 'post_single'

#     #Responde com 404 caso seja requisitado um post inexistente.
#     def get_object(self, queryset=None):
#         try:
#             return super().get_object(queryset)
#         except Http404:
#             raise Http404("O item solicitado não existe.")

# class CreatePostView(CreateView):
#     model = Post
#     #form_class = PostForm
#     template_name = 'create_post.html'
#     fields = '__all__'

# class EditPostView(UpdateView):
#     model = Post
#     template_name = 'edit_post.html'
#     fields = ['title', 'content', 'post_date']

# class RemovePostView(DeleteView):
#     model = Post
#     template_name = 'remove_post.html'
#     success_url = reverse_lazy('home')

#     #Implementar uma página de confirmação
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['confirmar_exclusao'] = True  # Adiciona uma variável de confirmação ao contexto
#         return context