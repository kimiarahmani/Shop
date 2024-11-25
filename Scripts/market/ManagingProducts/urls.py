from django.urls import path  
from . import views  
from .views import ClearProductsView
  
urlpatterns = [  
   path('api/products/', views.ProductAddGetView.as_view()),
   path('api/products/<int:pk>/', views.ProductUpdateDeleteView.as_view()), 
   path('api/products/clear/', ClearProductsView.as_view(), name='clear-products'),
]