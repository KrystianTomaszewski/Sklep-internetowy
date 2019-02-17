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
    description = models.CharField(max_length=200,
                                   default='Opis produktu')
    size = models.CharField(
        max_length=100,
        choices=c,
        default=d,
    )

    def __str__(self):
        kategorie = ""
        for kat in self.category_set.all():
            kategorie += kat.name + ','
        return self.name + " - " + kategorie





