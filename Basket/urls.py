from django.urls import path
# from rest_framework.routers import SimpleRouter
from . import views

app_name = 'Basket'


urlpatterns = [
    path('', views.OrderList.as_view(), name='list'),
]