from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

from .models import Bet, BetLine
from betCart.betCart import BetCart

# Create your views here.

@login_required(login_url='/auth/login')
def place_bet(request):
    bet = Bet.objects.create(user=request.user)
    bet_cart = BetCart(request)
    bet_lines = list()
    for key, value in bet_cart.items():
        bet_lines.append(BetLine(
            match_id = key,
            match_bet = value['match_bet'],
            team_bet = value['team_bet'],
            user_id = request.user.id,
            bet = bet
        ))
    BetLine.objects.bulk_create(bet_lines)
    bet_mail(bet = bet, bet_lines = bet_lines, first_name = request.user.first_name, last_name = request.user.last_name, email = request.user.email)
    messages.success(request, 'The order has been created successfully')
    return redirect('teamBets:bet')

def bet_mail(**kwargs):
    subject = 'Thanks for placing bets with us'
    msg = render_to_string('bettingCart/bet.html',{
        'bet': kwargs.get('bet'),
        'bet_lines': kwargs.get('bet_lines'),
        'first_name': kwargs.get('first_name'),
        'last_name': kwargs.get('last_name'),
        'email': kwargs.get('email')
    })
    msg_text = strip_tags(msg)
    from_email = 'danarv1412@gmail.com'
    to = kwargs.get('email')
    send_mail(subject,msg_text,from_email,[to],html_message=msg,fail_silently=False)
