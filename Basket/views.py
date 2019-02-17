from django.shortcuts import render
from .models import Basket, Order
from django.views import generic


class BasketList(generic.ListView):
    model = Order