from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import F, Sum, FloatField

from shop.models import Product

# Create your models here.

User = get_user_model()

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'orders'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ['id']

    def __str__(self):
        return self.id # type: ignore
    
    @property
    def total(self):
        return self.orderLine_set.aggregate( # type: ignore
            total = Sum(F("price")*F("quantity"), output_field=FloatField())
        )["total"]

class OrderLine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Order Line'
        verbose_name_plural = 'Order Lines'
        ordering = ['id']
        db_table = 'orderLines'

    def __str__(self):
        return f'{self.quantity} units of {self.product.name}'