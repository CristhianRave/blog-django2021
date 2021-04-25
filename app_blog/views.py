from django.shortcuts import render
from .models import Article, Category

# Create your views here.
def articles (request):

    articles = Article.objects.all()
    return render (request, 'articles/list.html', {
        'articles' : articles
    })