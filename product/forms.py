from django import forms
from .models import Product

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

    DISCOUNT_PERCENTAGE_CHOICES = [
        (0, '0%'),
        (10, '10%'),
        (20, '20%'),
        (30, '30%'),
        (40, '40%'),
        (50, '50%'),
        (60, '60%'),
        (70, '70%'),
        (80, '80%'),
        (90, '90%'),
    ]

    series = forms.ChoiceField(choices=SERIES_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    sub_category = forms.ChoiceField(choices=SUB_CATEGORY_CHOICE, widget=forms.Select(attrs={'class': 'form-control'}))
    related_products = forms.ModelMultipleChoiceField(queryset=Product.objects.all(), required=False, widget=forms.SelectMultiple(attrs={'class': 'form-control'}))
    discount_amount = forms.ChoiceField(choices=DISCOUNT_PERCENTAGE_CHOICES, widget=forms.Select(attrs={'class','form-control'}))
    
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
        # Raises validation errors under specific crieria.
        # Form variables for size validation
        cleaned_data = super().clean()
        category = cleaned_data.get('category')
        size = cleaned_data.get('size')
        # Form variables for discount items
        discounted = cleaned_data.get('discounted')
        discount_amount = cleaned_data.get('discount_amount')
        # Form variables for Appending search tags
        category = cleaned_data.get('category')
        series = cleaned_data.get('series')
        sub_category = cleaned_data.get('sub_category')
        name = cleaned_data.get('name')

        # Ensures that a % is filled out when discounted is selected.
        if discounted and not discount_amount:
            raise forms.ValidationError('You Must select a discount amount')
        
        # Ensures a size is selected when Clothing is set as the category.
        elif category == 'Clothing' and not size:
            raise forms.ValidationError("Size is required for clothing items.")
        
        # Empty list for the search tags
        search_tags = []
        
        # Appends all of the following fields into the search tags. 
        if category:
            search_tags.append(category)
        if series:
            search_tags.append(series)
        if sub_category:
            search_tags.append(sub_category)
        if name:
            search_tags.append(name)

        # Seperates the search fields with commas.
        cleaned_data['search_tags'] = ', '.join(search_tags)
        
        return cleaned_data
