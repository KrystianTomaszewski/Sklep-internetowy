from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse

from .models import Product
from category.models import Category


# Create your views here.


def index(request):
    products_list = Product.objects.all()
    kategorie = Category.objects.all()
    context = {'products_list': products_list, 'categories_list': kategorie}
    return render(request, 'products/index.html', context)


class DetailView(generic.DetailView):
    model = Product
    template_name = 'products/detail_page.html'
