from .models import Comment
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import generic


# from Product.models import Product

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'Comments/index.html'
    context_object_name = 'comments_list'

    def get_queryset(self):
        comments_list = Comment.objects.all()
        return comments_list

class DetailView(generic.DetailView):
     model = Comment
     template_name = 'Comments/detail.html'


