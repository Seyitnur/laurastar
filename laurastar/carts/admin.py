from django.contrib import admin
from unfold.admin import ModelAdmin, StackedInline, TabularInline
from .models import *

admin.site.register(OrderItem)

class ItemInline(StackedInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('product', 'quantity')

@admin.register(Order)
class OrderAdmin(ModelAdmin):
    inlines = [ItemInline]
    list_display = ('id', 'customer_name', 'customer_phone', 'customer_email', 'status')