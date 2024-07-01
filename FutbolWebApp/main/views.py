from django.shortcuts import render
from shoppingCart.shoppingCart import ShoppingCart

# Create your views here.

def index(request):
    shopping_cart = ShoppingCart(request)
    return render(request, 'index.html')