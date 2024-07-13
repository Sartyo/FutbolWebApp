from django.conf import settings

class BetCart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        bet_cart = self.session.get(settings.BET_CART_SESSION_ID)
        if not bet_cart:
            bet_cart = self.session[settings.BET_CART_SESSION_ID] = {}
        self.bet_cart = bet_cart

    def add_bet(self, match, match_bet, team_bet):
        if (str(match.id) not in self.bet_cart.keys()):
            self.bet_cart[match.id] = {
                'match_id': match.id,
                'team_1': match.team_1,
                'team_2': match.team_2,
                'match_date': match.match_date,
                'match_bet': match_bet,
                'team_bet': team_bet
            }
        else:
            for key, value in self.bet_cart.items():
                if key == str(match.id):
                    value['team_bet'] = team_bet
                    value['match_bet'] = match_bet
                    break
        self.save_bet_cart()

    def save_bet_cart(self):
        self.session[settings.BET_CART_SESSION_ID] = self.bet_cart
        self.session.modified = True

    def delete_bet(self, match):
        match.id = str(match.id)
        if match.id in self.bet_cart:
            del self.bet_cart[match.id]
            self.save_bet_cart

    def clear_bet_cart(self):
        self.session[settings.BET_CART_SESSION_ID]= {}
        self.session.modified = True