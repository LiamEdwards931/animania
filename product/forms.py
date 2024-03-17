from django import forms
from .models import Product,product_banner
from django.core.validators import MinValueValidator, MaxValueValidator


class ProductForm(forms.ModelForm):
    SERIES_CHOICES = [
        ('Naruto', 'Naruto'),
        ('Dragon Ball', 'Dragon Ball'),
        ('One Piece', 'One Piece'),
        ('Bleach', 'Bleach'),
        ('My Hero Academia', 'My Hero Academia'),
        ('Death Note', 'Death Note'),
        ('Fullmetal Alchemist', 'Fullmetal Alchemist'),
        ('Attack on Titan', 'Attack on Titan'),
        ('Hunter x Hunter', 'Hunter x Hunter'),
        ('One Punch Man', 'One Punch Man'),
        ('Fairy Tail', 'Fairy Tail'),
        ('Black Clover', 'Black Clover'),
        ('Demon Slayer', 'Demon Slayer'),
        ('Sword Art Online', 'Sword Art Online'),
        ('Tokyo Ghoul', 'Tokyo Ghoul'),
        ('Attack On Titan', 'Attack On Titan'),
        ('Shangri la frontier', 'Shangri la frontier'),
        ('Solo Leveling', 'Solo Leveling'),
        ('That Time I Got Reincarnated as a Slime', 'That Time I Got Reincarnated as a Slime'),
        ('The Rising of the Shield Hero', 'The Rising of the Shield Hero'),
        ('Akame ga Kill', 'Akame ga Kill'),
        ('Seven Deadly Sins', 'Seven Deadly Sins'),
        
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

    series = forms.ChoiceField(
        choices=SERIES_CHOICES, 
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    category = forms.ChoiceField(
        choices=CATEGORY_CHOICES, 
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    sub_category = forms.ChoiceField(
        choices=SUB_CATEGORY_CHOICE, 
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    related_products = forms.ModelMultipleChoiceField(
        queryset=Product.objects.all(), 
        required=False, 
        widget=forms.SelectMultiple(attrs={'class': 'form-control'})
    )
    
    discount_amount = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        required=False
    )
 
    class Meta:
        model = Product
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control-textarea'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'cost_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantity_available': forms.NumberInput(attrs={'class': 'form-control'}),
            'new': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'discounted': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'size': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        category = cleaned_data.get('category')
        size = cleaned_data.get('size')
        discounted = cleaned_data.get('discounted')
        discount_amount = cleaned_data.get('discount_amount')
        series = cleaned_data.get('series')
        sub_category = cleaned_data.get('sub_category')
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')
        price = cleaned_data.get('price')

        if discounted and not discount_amount:
            raise forms.ValidationError('You must select a discount amount.')

        if discount_amount is not None:
            if discount_amount < 0:
                raise forms.ValidationError('You cannot select a value less than 0 for the discount amount.')
            elif discount_amount > 100:
                raise forms.ValidationError('You cannot select a value higher than 100 for the discount amount.')
            elif discount_amount % 1 != 0:
                raise forms.ValidationError('Discount amount must be a whole number.')

        if category == 'Clothing' and not size:
            raise forms.ValidationError("Size is required for clothing items.")

        search_tags = [tag for tag in [category, series, sub_category, name] if tag]
        cleaned_data['search_tags'] = ', '.join(search_tags)

        if not name or not description or not price:
            raise forms.ValidationError("All required fields must be filled in.")

        return cleaned_data
    
class BannerForm(forms.ModelForm):
    
    SERIES_CHOICES = [
        ('Naruto', 'Naruto'),
        ('Dragon Ball', 'Dragon Ball'),
        ('One Piece', 'One Piece'),
        ('Bleach', 'Bleach'),
        ('My Hero Academia', 'My Hero Academia'),
        ('Death Note', 'Death Note'),
        ('Fullmetal Alchemist', 'Fullmetal Alchemist'),
        ('Attack on Titan', 'Attack on Titan'),
        ('Hunter x Hunter', 'Hunter x Hunter'),
        ('One Punch Man', 'One Punch Man'),
        ('Fairy Tail', 'Fairy Tail'),
        ('Black Clover', 'Black Clover'),
        ('Demon Slayer', 'Demon Slayer'),
        ('Sword Art Online', 'Sword Art Online'),
        ('Tokyo Ghoul', 'Tokyo Ghoul'),
        ('Attack On Titan', 'Attack On Titan'),
        ('Shangri la frontier', 'Shangri la frontier'),
        ('Solo Leveling', 'Solo Leveling'),
        ('That Time I Got Reincarnated as a Slime', 'That Time I Got Reincarnated as a Slime'),
        ('The Rising of the Shield Hero', 'The Rising of the Shield Hero'),
        ('Akame ga Kill', 'Akame ga Kill'),
        ('Seven Deadly Sins', 'Seven Deadly Sins'),
        
    ]

    series = forms.ChoiceField(
        choices=SERIES_CHOICES, 
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    class Meta:
        model = product_banner
        fields = ("image","series")
