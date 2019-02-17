from django.shortcuts import render
from .models import Order
from django.views import generic


class OrderList(generic.ListView):
    model = Order

# class CategoryViewSet(viewsets.ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer