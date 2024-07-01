from django.contrib import admin
from .models import Product, TagProduct

# Register your models here.

class TagProductAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(TagProduct, TagProductAdmin)
admin.site.register(Product, ProductAdmin)