from .models import Comments
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import generic
from Product.models import Product

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'Comments/index.html'
    context_object_name = ''

