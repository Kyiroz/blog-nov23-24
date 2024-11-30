from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Post
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