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
            'video_url': 'Video URL'
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
