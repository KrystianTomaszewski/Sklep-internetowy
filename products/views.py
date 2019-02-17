from django.shortcuts import render
from django.views import generic

from .models import Product

# Create your views here.


def index(request):
    categories = Product.objects.all()
    beauty_form = [str(cat) + ', ' for cat in categories]
    # template = loader.get_template('catalogs/catalogs.html')
    # context = {
    #     'category_list': categories,
    # }
    # return render(request, 'catalogs/catalogs.html',context, category_list)

    return HttpResponse(beauty_form)
