from django.shortcuts import render

# generic-class-based Listview to list the contents of the database model

# generic class- based Deatilview

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post

from django.urls import reverse_lazy


class BolgListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailview(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'rex'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')