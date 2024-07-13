from django.urls import path
from . import views

app_name = 'teamBets'

urlpatterns = [
    path('', views.matches, name='matches')
]