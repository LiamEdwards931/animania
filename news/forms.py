from django import forms
from .models import News


class newsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = ['title', 'news_image', 'short_description',
                  'description', 'video_url']

    def __init__(self, *args, **kwargs):
        super(newsForm, self).__init__(*args, **kwargs)
        placeholders = {
            'title': 'Title',
            'news_image': 'News Image',
            'short_description': 'Short Description',
            'description': 'Description',
            'video_url': 'https://www.youtube.com/watch?v=PraFso1sVIc'
        }
        for field_name, field in self.fields.items():
            if field.required:
                placeholders[field_name] += ' * required'
            field.widget.attrs['placeholder'] = placeholders[field_name]
            field.widget.attrs['class'] = 'news-form'
            if field_name == 'description':
                field.widget = forms.Textarea(attrs={'rows': 10, 'cols': 50})
            elif field_name == 'short_description':
                field.widget = forms.Textarea(attrs={'rows': 5, 'cols': 50})
            elif field_name == 'title':
                field.widget = forms.Textarea(attrs={'rows': 1,  'cols': 50})


class NewsSignup(forms.Form):
    name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your full name'
        }),
        label="Full Name"
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email address'
        }),
        label="Email Address"
    )
    offers = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input'
        }),
        label="Receive Offers"
    )

    def __init__(self, *args, **kwargs):
        super(NewsSignup, self).__init__(*args, **kwargs)
