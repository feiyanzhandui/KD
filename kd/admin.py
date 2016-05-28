from django.contrib import admin
from .models import Order

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender_name','sender_city','sender_contact','receiver_name','receiver_city', 'receiver_contact')

admin.site.register(Order, OrderAdmin)
