from django.shortcuts import render
from .models import Product, TagProduct
from shoppingCart.views import clear_shopping_cart

# Create your views here.

def shop(request):
    tags = TagProduct.objects.all()
    products = Product.objects.all()
    return render(request, 'shop.html', {'products': products, 'tags': tags})

def tagProduct(request, tag_id):
    tags = TagProduct.objects.all()
    tag = TagProduct.objects.get(id = tag_id)
    products = Product.objects.filter(tag = tag)
    return render(request, 'tagProduct.html', {'products': products, 'tags': tags, 'tag': tag})

def order(request):
    clear_shopping_cart(request)
    return render(request, 'order.html')