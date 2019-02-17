from django.db import models
from products.models import Product
from django.contrib.auth.models import User

class Basket(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        klient = str(self.client)
        return klient

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=0)
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)


    def checkout(self):
        return self.product.price * self.amount

    def __str__(self):
        tresc = self.basket.client.username + " " + "Choosen: " + self.product.name + " - Total price: " + str(self.checkout()) + " $"
        return tresc
