from django.db import models
from django.contrib.auth import get_user_model
from teamBets.models import Match, Team

# Create your models here.

User = get_user_model()

class Bet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'bets'
        verbose_name = 'Bet'
        verbose_name_plural = 'Bets'
        ordering = ['id']

    def __str__(self):
        return self.id
    
    @property
    def total(self):
        total = 0
        for betLine in self.betLines.all():
            delta = 0
            team_bet_skill = betLine.team_bet.skill
            opposite_team_skill = 0
            if betLine.team_bet.id == betLine.match.team_1.id:
                opposite_team_skill = betLine.match.team_2.skill
            else:
                opposite_team_skill = betLine.match.team_1.skill
            skill_diff = (team_bet_skill - opposite_team_skill)
            if skill_diff < 0:
                skill_diff = abs(skill_diff)
                delta = (skill_diff + 10) / 10
                total = total + (betLine.money_bet * delta)
            elif skill_diff == 0:
                total = total + betLine.money_bet
            else:
                delta = 10 / (skill_diff + 10)
                total = total + (betLine.money_bet * delta)
        return total


class BetLine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bet = models.ForeignKey(Bet, on_delete=models.CASCADE, related_name='betLines')
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    team_bet = models.ForeignKey(Team, on_delete=models.CASCADE)
    money_bet = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Bet Line'
        verbose_name_plural = 'Bet Lines'
        ordering = ['id']
        db_table = 'betLines'

    def __str__(self):
        return f'{self.money_bet}$ bet for {self.team_bet.name} in the match: \n{self.match.__str__}'