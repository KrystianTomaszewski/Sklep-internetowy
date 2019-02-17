from django.db import models
from products.models import Product
from django.contrib.auth.models import User

class Order(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=0)


    #
    # @receiver(post_save, sender=Entry)
    # def update_basket(sender, instance, **kwargs):
    #     cost = instance.count * instance.product.price
    #     instance.basket.count = int(instance.basket.count) + int(instance.count)
    #
    #
