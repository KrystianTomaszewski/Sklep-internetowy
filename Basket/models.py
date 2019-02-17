from django.db import models
from products.models import Product, Id
from django.contrib.auth.models import Users

Users = models.ForeignKey(Users)
Product = models.ForeignKey(Product)

class Number(models.Model):
    count = models.PositiveIntegerField(default=0)


#     def counting(self, Product)
#         product_Id = models.ForeignKey(Product)
#             if product_Id in self.Basket:
#       return count(self.Basket[product_Id])
#
#
# if product_id in self.Basket:
#     self.Basket['product_id']['quantity'


    class Entry(models.Model):
        product = models.ForeignKey(Product, null=True)
        count = models.PositiveIntegerField()

    @receiver(post_save, sender=Entry)
    def update_basket(sender, instance, **kwargs):
        line_cost = instance.quantity * instance.product.price
        instance.cart.count = int(instance.cart.count) + int(instance.quantity)