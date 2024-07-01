from django.db import models

# Create your models here.

class TagProduct(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'TagProduct'
        verbose_name_plural = 'TagsProducts'

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.BooleanField(default=True)
    image = models.ImageField(upload_to='shop', null=True, blank=True)
    tag = models.ForeignKey(TagProduct, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name