from django.db import models
from products.models import Product

# Create your models here.
class Category(models.Model):

    name = models.CharField(max_length=10)
    product = models.ManyToManyField(Product, null=True, blank=True)

