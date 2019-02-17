from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse


from .models import Product

# Create your views here.



def index(request):

    products_list = Product.objects.all()

    context = {'products_list': products_list}

    return render(request, 'products/index.html', context)


class DetailView(generic.DetailView):
    model = Product
    template_name = 'products/detail_page.html'

