from django.urls import include, path
from . import views

urlpatterns = [
    
    path('articulos/', views.articles, name='lista_Articulos' ),
    
]