from django.urls import path
from . import views

urlpatterns = [
    path('', views.heart_disease_form, name='heart_disease_form'),
]
 