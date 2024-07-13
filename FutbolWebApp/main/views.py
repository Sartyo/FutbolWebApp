from django.shortcuts import render
from shoppingCart.shoppingCart import ShoppingCart
from betCart.betCart import BetCart

# Create your views here.

def index(request):
    bet_cart = BetCart(request)
    shopping_cart = ShoppingCart(request)
    return render(request, 'index.html')