from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('electronics/', views.electronics, name='electronics'),  
    path('clothing/', views.clothing, name='clothing'),  
    path('home_goods/', views.home_goods, name='home_goods'),  
    path('beauty/', views.beauty, name='beauty'), 
]