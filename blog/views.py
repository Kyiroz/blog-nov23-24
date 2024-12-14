from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy
# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html' #Archivo dentro de la carpeta templates

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html' #Archivo dentro de la carpeta templates(Detail)

class PostCreateView(CreateView):
    model = Post
    template_name = 'post_new.html' #Archivo dentro de la carpeta templates(Create)
    fields = ['title', 'content', 'author'] #Campos que se van a mostrar en el formulario

class PostUpdateView(UpdateView):
    model = Post
    template_name = "post_update.html"
    fields = ['title', 'content'] #Campos que se van a mostrar en el formulario

class PostDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy('blog-home') #Al eliminar, te redirecciona a la url home