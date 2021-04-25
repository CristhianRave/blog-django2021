from django.urls import include, path
from mainapp import views

urlpatterns = [
    
    path('', views.index, name='home' ),
    path('index/', views.index, name='inicio' ),
    path('blog/', views.blog, name='Blog' ),
]