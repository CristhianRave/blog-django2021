from django.urls import include, path
from pages import views

urlpatterns = [
    
    path('page/<str:slug>', views.page, name='pagina' ),
    
]