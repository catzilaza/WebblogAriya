from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [    
    path('', views.index, name='index'),#
    path('seminar99708Jan/', views.seminar99708Jan, name='seminar99708Jan'), 
    path('seminar99708Dec/', views.seminar99708Dec, name='seminar99708Dec'),
    path('seminar99709Dec/', views.seminar99709Dec, name='seminar99709Dec'),
    path('phuket/', views.phuket, name='phuket'),
    path('resources_research/', views.resources_research, name='resources_research'),
    path('checkout_payment/', views.checkout_payment, name='checkout_payment')   
]
