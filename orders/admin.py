from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'email', 'status', 'total_amount', 'created_at']
    list_filter = ['status', 'created_at']
    list_editable = ['status']
    inlines = [OrderItemInline]
    search_fields = ['user__username', 'email', 'phone']
