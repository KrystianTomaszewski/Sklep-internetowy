from django.contrib import admin
from .models import Order
from .models import Basket


admin.site.register(Order)
admin.site.register(Basket)
