from django.contrib import admin
from .models import Order, OrderLine
# Register your models here.


class OrderLineAdminInLine(admin.TabularInline):
    model = OrderLine
    readonly_fields = ('subtotal',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInLine,)
    readonly_fields = ('order_number', 'delivery_cost',
                       'total_cost', 'grand_total', 'date')

    field = ('order_number', 'first_name', 'last_name', 'email',
             'door_number', 'street', 'city', 'county', 'country',
             'postal_code')

    list_display = ('order_number', 'first_name', 'last_name',
                    'date', 'total_cost', 'delivery_cost',
                    'grand_total')

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
