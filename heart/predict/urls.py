from django.urls import path
from . import views

urlpatterns = [
    path('', views.heart_disease_form, name='heart_disease_form'),
    path('generate_pdf/', views.generate_pdf, name='generate_pdf'),  
]
 
 
