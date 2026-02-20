from django.contrib import admin
from .models import Order, OrderItem

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'status', 'created_at')
    search_fields = ('customer__email',)
    list_filter = ('status', 'created_at')

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity', 'price')
    search_fields = ('order__id', 'product__name')
    list_filter = ('order__status',)

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
