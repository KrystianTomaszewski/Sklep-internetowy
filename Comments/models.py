from django.db import models
from django.contrib.auth.models import User
from products.models import Product


# Create your models here.
class Comments:
    g = [("1", "Słabe"), ("2", "Akceptowalne"), ("3", "Średnie"), ("4", "Dobre"), ("5", "Fantastyczne")]
    user = User
    product = Product.id,
    text = models.CharField(max_length=300)
    pub_date = models.DateTimeField('Opublikowane')
    grade = models.ChoiceField(g)
