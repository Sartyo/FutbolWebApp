from django.urls import path
from . import views

app_name = "shoppingCart"

urlpatterns = [
    path("add/<int:product_id>/", views.add_product, name="addProduct"),
    path("remove/<int:product_id>/", views.remove_product, name="removeProduct"),
    path("delete/<int:product_id>/", views.delete_product, name="deleteProduct"),
    path("clear", views.clear_shopping_cart, name="clearShoppingCart"),
]