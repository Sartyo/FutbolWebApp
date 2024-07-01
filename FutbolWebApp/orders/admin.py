from django.contrib import admin

from orders.models import Order, OrderLine

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class OrderLineAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLine, OrderLineAdmin)