from django.db import models
from products.models import Product

from django.contrib.auth.models import User

class Order(models.Model):
    client = models.ForeignKey(User)
    product = models.ForeignKey(Product)
    amount = models.PositiveIntegerField(default=0)


    #
    # @receiver(post_save, sender=Entry)
    # def update_basket(sender, instance, **kwargs):
    #     cost = instance.count * instance.product.price
    #     instance.basket.count = int(instance.basket.count) + int(instance.count)
    #
    #
