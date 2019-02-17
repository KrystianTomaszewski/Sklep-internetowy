from django.views import generic
from .models import Category
# Create your views here.

class CategoryList(generic.ListView):
    model = Category

    def __str__(self):
        return self.Category.name

category_list = CategoryList.as_view()

class UbranieView(generic.ListView):
    model = Category
    template_name = 'category/ubranie.html'


class ButyView(generic.ListView):
    model = Category
    template_name = 'category/Buty.html'