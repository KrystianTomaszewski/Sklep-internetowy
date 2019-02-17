from django.db import models
from django.contrib.auth.models import User
from products.models import Product


# Create your models here.
class Comment(models.Model):
    g = [("1", "Słabe"), ("2", "Akceptowalne"), ("3", "Średnie"), ("4", "Dobre"), ("5", "Fantastyczne")]
    user = User
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    pub_date = models.DateTimeField('Opublikowane')
    grade = models.CharField(max_length=2, choices=g)

    def __str__(self):
        #return "Czesc, to jest komentarz dla:" + self.product.name
        return self.product.name
