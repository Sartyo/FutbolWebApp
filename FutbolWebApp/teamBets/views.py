from django.shortcuts import render
from .models import Match
from betCart.views import clear_bet_cart

# Create your views here.

def matches(request):
    matches = Match.objects.all()
    return render(request, 'matches.html', {'matches': matches})

def bet(request):
    clear_bet_cart(request)
    return render(request, 'bet.html')

def match(request, match_id):
    match = Match.objects.get(id = match_id)
    return render(request, 'match.html', {'match': match})