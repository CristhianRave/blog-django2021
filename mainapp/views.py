from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'mainapp/index.html', {
        'title' : 'Inicio'
    })


# -----------------------------------------------------------

def blog (request):

    
    return render (request, 'mainapp/blog.html', {
        'title' : 'Blog'
    })
    
# -----------------------------------------------------------
    
def portfolio (request):

    
    return render (request, 'mainap/portfolio.html', {
        'title' : 'Portfolio'
    })


# -----------------------------------------------------------

def about (request):

    
    return render (request, 'mainapp/about.html', {
        'title' : 'Sobre nosotros'
    })



    