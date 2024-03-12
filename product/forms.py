from django import forms
from .models import Product
from django.utils.text import slugify


class ProductForm(forms.ModelForm):
    SERIES_CHOICES = [
        ('Demon Slayer', 'Demon Slayer'),
        ('Sword Art Online', 'Sword Art Online'),
        ('Tokyo Ghoul', 'Tokyo Ghoul'),
        ('Attack On Titan','Attack On Titan'),
        ('Shangri la frontier','Shangri la frontier'),
        ('Solo Leveling','Solo Leveling'),
        ('Reincarnated as a slime','Reincarnated as a slime'),
        ('Akame ga kill','Akame ga kill'),
        ('Seven Deadly Sins','Seven Deadly Sins'),
        
    ]

    series = forms.ChoiceField(choices=SERIES_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Product
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control-textarea'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity_available': forms.NumberInput(attrs={'class': 'form-control'}),
            'new': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'discounted': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'size': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        category = cleaned_data.get('category')
        size = cleaned_data.get('size')

        if category == 'clothing' and not size:
            raise forms.ValidationError("Size is required for clothing items.")

        return cleaned_data