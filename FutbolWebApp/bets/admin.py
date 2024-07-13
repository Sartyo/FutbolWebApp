from django.contrib import admin
from .models import Bet, BetLine

# Register your models here.

class BetAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class BetLineAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Bet, BetAdmin)
admin.site.register(BetLine, BetLineAdmin)