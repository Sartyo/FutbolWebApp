from django.db import models

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    logo = models.ImageField(upload_to='teams', blank=True, null=True)
    skill = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'

    def __str__(self):
        return self.name

class Match(models.Model):
    team_1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name= 'team_1')
    team_2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name= 'team_2')
    match_date = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Match'
        verbose_name_plural = 'Matches'

    def __str__(self):
        return f"{self.team_1} vs {self.team_2} at {self.match_date}"