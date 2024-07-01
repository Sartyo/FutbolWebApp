from django.urls import path

from orders import views

app_name = 'orders'


urlpatterns = [
    path('', views.make_order, name='makeOrder'),
]