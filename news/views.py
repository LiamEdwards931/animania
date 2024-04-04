from django.shortcuts import render, redirect
from django.contrib import messages
from . import forms

# Create your views here.

def news(request):
    return render(request,'news.html')

def create_news(request):
    if request.method == 'POST':
        form = forms.newsForm(request.POST, request.FILES)
        if form.is_valid():
                form.save()
                messages.success(request, 'Successfully Created your news article')
                return redirect('news')
        else:
            messages.error(request, 'Could not upload your form, double check your inputs')
    else: 
        form = forms.newsForm()

    context = {
        'form': form
    }
    return render(request,'create_news.html', context)