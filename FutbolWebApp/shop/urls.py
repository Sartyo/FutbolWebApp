from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.shop, name='shop'),
    path('tag/<int:tag_id>/', views.tagProduct, name='tagProduct'),
    path('order-success/', views.order, name='order')
]