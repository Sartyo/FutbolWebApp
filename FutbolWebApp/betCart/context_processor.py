from django.conf import settings


def total_import_bet_cart(request):
    total = 0
    if request.user.is_authenticated:
        for key, value in request.session[settings.BET_CART_SESSION_ID].items():
            total = total + float(value["price"])
    else:
        total = "You must login to place bets"
    return {"total_import_bet_cart": total}