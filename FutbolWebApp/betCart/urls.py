from django.urls import path
from . import views

app_name = 'betCart'

urlpatterns = [
    path('', views.place_bet, name='placeBet')
]