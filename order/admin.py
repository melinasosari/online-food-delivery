from django.contrib import admin
from .models import Order, OrderItem
from django.urls import reverse
from django.utils.safestring import mark_safe

class OrderItemInline(admin.TabularInline):
   model = OrderItem
   raw_id_fields = ['food']


def order_detail(obj):
   url = reverse("admin_order_detail", args=[obj.id])
   return mark_safe(f'<a href="{url}">View</a>')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'postal_code', 'paid', 'address', order_detail]
    list_filter = ['paid', 'created_at', 'updated_at']
    inlines = [OrderItemInline]
