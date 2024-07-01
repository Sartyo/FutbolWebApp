from django.conf import settings

class ShoppingCart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        shopping_cart = self.session.get(settings.CART_SESSION_ID)
        if not shopping_cart:
            shopping_cart = self.session[settings.CART_SESSION_ID] = {}
        # else:
        self.shopping_cart = shopping_cart

    def add_product(self, product):
        if(str(product.id) not in self.shopping_cart.keys()):
            self.shopping_cart[product.id] = {
                "product_id": product.id,
                "name": product.name,
                "price": str(product.price),
                "quantity": 1,
                "image": product.image.url
            }
        else:
            for key, value in self.shopping_cart.items():
                if key == str(product.id):
                    value['quantity'] = value["quantity"] + 1
                    value['price'] = float(value['price']) + product.price
                    break
        self.save_shopping_cart()

    def save_shopping_cart(self):
        self.session["cart"] = self.shopping_cart
        self.session.modified = True

    def delete_product(self, product):
        product.id = str(product.id)
        if product.id in self.shopping_cart:
            del self.shopping_cart[product.id]
            self.save_shopping_cart()

    def remove_product(self, product):
        for key, value in self.shopping_cart.items():
                if key == str(product.id):
                    value['quantity'] = value["quantity"] - 1
                    value['price'] = float(value['price']) - product.price
                    if value['quantity'] < 1:
                        self.delete_product(product)
                    break
        self.save_shopping_cart()

    def clear_shopping_cart(self):
        self.session['cart']= {}
        self.session.modified = True