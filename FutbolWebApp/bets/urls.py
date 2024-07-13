from django.urls import path
from . import views

app_name = 'bets'

urlpatterns = [
    path('', views.place_bet, name='placeBet')
]