from django.urls import path
from . import views

app_name = 'category'

urlpatterns = [
    path('', views.CategoryList.as_view(), name='categorylist'),
    path('1/', views.UbranieView.as_view(), name='ubranie'),
    path('2/', views.ButyView.as_view(), name='buty'),
]