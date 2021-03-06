from django.contrib import admin

from .models import Order, OrderItem


class OrderItemsInline(admin.TabularInline):
    model = Order.items.through
    fields = ['products', 'quantity', 'price']
    readonly_fields = ['products', 'quantity', 'price']
    extra = 0

    def products(self, instance):
        return instance.orderitems

    def quantity(self, instance):
        return instance.orderitems.quantity

    def price(self, instance):
        return instance.order_items.price


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemsInline]
    exclude = ['items']
    list_display = (
        'id', 'user', 'status', 'created_at', 'total'
    )

admin.site.register(Order, OrderAdmin)
# admin.site.register(OrderItem)
