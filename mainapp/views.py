from django.shortcuts import render
from app_blog.models import Article, Category

# Create your views here.

def index(request):
    return render(request,'mainapp/index.html', {
        'title' : 'Inicio'
    })


# -----------------------------------------------------------

def blog (request):

    articles = Article.objects.all ()
    return render (request, 'mainapp/blog.html', {
        'title' : 'Blog',
        'articles' : articles

    })
    
# -----------------------------------------------------------
    

def about (request):

    
    return render (request, 'mainapp/about.html', {
        'title' : 'Sobre nosotros'
    })



    