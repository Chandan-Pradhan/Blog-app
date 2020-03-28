from django.shortcuts import render

# generic-class-based Listview to list the contents of the database model

# generic class- based Deatilview

from django.views.generic import ListView, DetailView

from .models import Post


class BolgListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailview(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'rex'



