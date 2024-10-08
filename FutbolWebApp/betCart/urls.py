from django.urls import path
from . import views

app_name = 'betCart'

urlpatterns = [
    path('add/', views.place_bet, name='place_bet'),
    path('delete/', views.delete_bet, name='delete_bet'),
    path('clear/', views.clear_bet_cart, name='clear_bet_cart')
]