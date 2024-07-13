from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

from shoppingCart.shoppingCart import ShoppingCart
from orders.models import Order, OrderLine

# Create your views here.

@login_required(login_url='/auth/login')
def make_order(request):
    order = Order.objects.create(user=request.user)
    cart = ShoppingCart(request)
    order_lines = list()
    for key, value in cart.shopping_cart.items():
        order_lines.append(OrderLine(
            product_id = key,
            quantity = value['quantity'],
            user_id = request.user.id,
            order = order
        ))
    OrderLine.objects.bulk_create(order_lines)
    order_mail(order = order, order_lines = order_lines, first_name = request.user.first_name, last_name = request.user.last_name, email = request.user.email)
    messages.success(request, 'The order has been created successfully')
    return redirect('shop:order')

def order_mail(**kwargs):
    subject = 'Thanks for purchasing with us'
    msg = render_to_string('shoppingCart/order.html',{
        'order': kwargs.get("order"),
        'order_lines': kwargs.get('order_lines'),
        'first_name': kwargs.get('first_name'),
        'last_name': kwargs.get('last_name'),
        'email': kwargs.get('email')
    })
    msg_text = strip_tags(msg)
    from_email = 'danarv1412@gmail.com'
    to = kwargs.get('email')
    send_mail(subject,msg_text,from_email,[to],html_message=msg,fail_silently=False) # type: ignore