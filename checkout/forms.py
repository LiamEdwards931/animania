from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
        class Meta:
            model = Order
            fields = ('first_name','last_name',
                      'email','door_number','street','city',
                      'county','country','postal_code')

        def __init__(self, *args, **kwargs):
            """
            Add placeholders and classes, remove auto-generated
            labels and set autofocus on first field
            """
            super().__init__(*args, **kwargs)
            placeholders = {
                'first_name': 'Full Name',
                'last_name': 'Last_Name',
                'email': 'Email Address',
                'door_number': 'Door Number',
                'country': 'Country',
                'postal_code': 'Post Code',
                'city': 'Town or City',
                'street': 'Street Address',
                'county': 'County',
            }

            self.fields['first_name'].widget.attrs['autofocus'] = True
            for field in self.fields:
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].widget.attrs['class'] = 'checkout-form'
                self.fields[field].label = False 
                
    
        
