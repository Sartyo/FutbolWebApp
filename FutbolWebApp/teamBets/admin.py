from django.contrib import admin
from .models import Team, Match

# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class MatchAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Team, TeamAdmin)
admin.site.register(Match, MatchAdmin)