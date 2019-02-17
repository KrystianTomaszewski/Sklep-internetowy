from django.db import models
from products.models import Product


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=10)
    product = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.name
