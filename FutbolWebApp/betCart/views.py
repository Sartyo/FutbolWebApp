from django.shortcuts import render,redirect

from .betCart import BetCart
from teamBets.models import Match

# Create your views here.

def place_bet(request):
    team_bet = request.POST['team_choice']
    match_bet = request.POST['bet_amount']
    match_id = request.POST['match_id']
    bet_cart = BetCart(request)
    match = Match.objects.get(id = match_id)
    bet_cart.add_bet(match, match_bet, team_bet)
    return redirect('teamBets:matches')

def delete_bet(request, match_id):
    bet_cart = BetCart(request)
    match = Match.objects.get(id = match_id)
    bet_cart.delete_bet(match)
    return redirect('teamBets:matches')

def clear_bet_cart(request):
    bet_cart = BetCart(request)
    bet_cart.clear_bet_cart()