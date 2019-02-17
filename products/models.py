from django.db import models

# Create your models here.

class Product(models.Model):

    c = [("1", "Option 1"), ("2", "Option 2")]

    name = models.CharField(max_length=100)
    price = models.FloatField
    # size = models.ChoiceField(choices=c, label='Size')

    def __str__(self):
        return self.name





