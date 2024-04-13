from django.contrib import admin
from .models import Address
# Register your models here.


class AddressAdmin(admin.ModelAdmin):
    list_display = (
            'user', 'door_number', 'street',
            'city', 'state', 'country', 'postal_code')
    search_fields = ('user__username', 'street', 'city',
                     'state', 'country', 'postal_code')
    list_filter = ('city', 'state', 'country')


admin.site.register(Address, AddressAdmin)
