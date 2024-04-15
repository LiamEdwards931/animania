from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from . import forms
from . models import News

# Create your views here.


def news(request):
    articles = News.objects.all()

    context = {
         'articles': articles
    }

    return render(request, 'news.html', context)


def create_news(request):
    if request.method == 'POST':
        form = forms.newsForm(request.POST, request.FILES)
        if form.is_valid():
            news_instance = form.save(commit=False)
            news_instance.author = request.user
            news_instance.save()
            messages.success(request, 'Successfully Created your news article')
            return redirect('news')
        else:
            messages.error(
                request,
                'Could not upload your form, double check your inputs')
    else:
        form = forms.newsForm()

    context = {
        'form': form
    }
    return render(request, 'create_news.html', context)


def news_detail(request, news_id):

    article = get_object_or_404(News, pk=news_id)

    context = {
         'article': article
     }

    return render(request, 'news_detail.html', context)

def delete_news(request, news_id):
    news = get_object_or_404(News, id=news_id)

    if request.user.is_superuser:
        news.delete()
        messages.success(request, 'News article deleted successfully.')
    else:
        messages.error(request, 'You Cannot delete this article')
    
    return redirect('news')
