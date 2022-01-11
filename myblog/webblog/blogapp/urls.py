from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [    
    path('', views.index, name='index'),#
    path('seminar99708Jan/', views.seminar99708Jan, name='seminar99708Jan'), 
    path('seminar99708Dec/', views.seminar99708Dec, name='seminar99708Dec'),
    path('seminar99709Dec/', views.seminar99709Dec, name='seminar99709Dec'),
    path('phuket/', views.phuket, name='phuket'),
    path('tempPage5/', views.tempPage5, name='temPage5'),
    path('tempPage6/', views.tempPage6, name='temPage6')   
]
