from django.db import models

# Create your models here.

class Product(models.Model):

    c = [("S", "Option S"),
         ("M", "Option M"),
         ("L", "Option L"),
         ("XL", "Option XL"),
         ("XXL", "Option XXL"),
         ("3XL", "Option 3XL"),
         ]

    d = ("XL", "Option 2"),

    name = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    size = models.CharField(
        max_length=100,
        choices=c,
        default=d,
    )

    def __str__(self):
        return self.name





