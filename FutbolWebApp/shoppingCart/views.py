from django.shortcuts import render, redirect
from .shoppingCart import ShoppingCart
from shop.models import Product

# Create your views here.

def add_product(request, product_id):
    shopping_cart = ShoppingCart(request)
    product = Product.objects.get(id = product_id)
    shopping_cart.add_product(product)
    return redirect("shop:shop")

def delete_product(request, product_id):
    shopping_cart = ShoppingCart(request)
    product = Product.objects.get(id = product_id)
    shopping_cart.delete_product(product)
    return redirect("shop:shop")

def remove_product(request, product_id):
    shopping_cart = ShoppingCart(request)
    product = Product.objects.get(id = product_id)
    shopping_cart.remove_product(product)
    return redirect("shop:shop")

def clear_shopping_cart(request):
    shopping_cart = ShoppingCart(request)
    shopping_cart.clear_shopping_cart()