from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import Address


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("username","first_name","last_name","email", "password1", "password2",)
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        self.fields['email'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
        self.fields['username'].widget.attrs['placeholder'] = 'Enter username'
        self.fields['first_name'].widget.attrs['placeholder'] = 'First name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm password'
        
class CustomPasswordChange(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['old_password'].help_text = ''
        self.fields['new_password1'].help_text = ''
        self.fields['new_password2'].help_text = ''

class AddressForm(forms.ModelForm):
    class Meta:
        door_number = forms.IntegerField(required=True)
        model = Address
        fields = ['door_number','street', 'city', 'state', 'country', 'postal_code']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['door_number'].widget.attrs['placeholder'] = 'Door number'
        self.fields['street'].widget.attrs['placeholder'] = 'Street'
        self.fields['city'].widget.attrs['placeholder'] = 'City'
        self.fields['state'].widget.attrs['placeholder'] = 'County'
        self.fields['country'].widget.attrs['placeholder'] = 'Country'
        self.fields['postal_code'].widget.attrs['placeholder'] = 'Post Code'
