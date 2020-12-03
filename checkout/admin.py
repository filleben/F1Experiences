from django.contrib import admin
from .models import Order, OrderLineItem

#Customised OrderLineItem Model for Admin View
class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)

#Customised Order Model for Admin view 
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)
    readonly_fields = ('order_number', 'date', 'order_total', 'original_cart', 'stripe_pid')
    list_display = ('order_number', 'full_name', 'date', 'order_total',)
    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)