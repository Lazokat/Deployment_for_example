from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from .models import Blog
class BlogView(ListView):
    model = Blog
    template_name = 'blog_list.html'
    context_object_name = 'blogs'
class BlogDetail(DetailView):
    model = Blog
    template_name = 'blog_detail.html'
    context_object_name = 'blogs'
class BlogCreate(CreateView):
    model = Blog
    template_name = 'blog_create.html'
    fields = ['title','body','image',]
    success_url = reverse_lazy('all_list')
class BlogDelete(DeleteView):
    model = Blog
    template_name = 'blog_delete.html'
    success_url = reverse_lazy('all_list')
class BlogUpdate(UpdateView):
    model=Blog
    template_name = 'blog_update.html'
    fields = ['title','body','image']
    success_url = reverse_lazy('all_list')
