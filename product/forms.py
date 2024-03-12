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

    CATEGORY_CHOICES = [
        ('Figures','Figures'),
        ('Pop-Vinyl','Pop-Vinyl'),
        ('Clothing','Clothing'),
        ('VideoGame','VideoGame')
    ]

    SUB_CATEGORY_CHOICE = [
        (None, None),
        ('hats', 'Hats'),
        ('hoodies', 'Hoodies'),
        ('t-shirt', 'T-Shirts'),
        ('jumper', 'Jumpers'),
        ('backpack', 'Backpacks'),
        ('ps4', 'PS4 Accessories'),
        ('xbox', 'Xbox Accessories'),
        ('soft-toy', 'Soft Toys'),
        ('action-figures', 'Action Figures'),
        ('collectible-statues', 'Collectible Statues'),
        ('model-kits', 'Model Kits'),
        ('miniatures', 'Miniatures'),
        ('dolls', 'Dolls'),
        ('funko-pop', 'Funko Pop!'),
        ('vinyl-figures', 'Vinyl Figures'),
        ('bobbleheads', 'Bobbleheads'),
        ('jackets', 'Jackets'),
        ('dresses', 'Dresses'),
        ('skirts', 'Skirts'),
        ('console-accessories', 'Console Accessories'),
        ('gaming-merchandise', 'Gaming Merchandise'),
        ('controller-skins', 'Controller Skins'),
        ('gaming-chairs', 'Gaming Chairs'),
        ('gaming-keyboards', 'Gaming Keyboards'),
        ('gaming-mice', 'Gaming Mice'),
    ]

    series = forms.ChoiceField(choices=SERIES_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    sub_category = forms.ChoiceField(choices=SUB_CATEGORY_CHOICE, widget=forms.Select(attrs={'class': 'form-control'}))
    related_products = forms.ModelMultipleChoiceField(queryset=Product.objects.all(), required=False, widget=forms.SelectMultiple(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Product
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control-textarea'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
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
    
    def clean(self):
        # Appends category, series, sub_category into the search tag field in the model.
        cleaned_data = super().clean()
        category = cleaned_data.get('category')
        series = cleaned_data.get('series')
        sub_category = cleaned_data.get('sub_category')

        search_tags = []

        if category:
            search_tags.append(category)
        if series:
            search_tags.append(series)
        if sub_category:
            search_tags.append(sub_category)

        # Join the search tags list into a single string and assign it to the search_tags field
        cleaned_data['search_tags'] = ', '.join(search_tags)

        return cleaned_data
