from django.urls import path  
from . import views
from .views import ClearCategoriesView
  
urlpatterns = [  
   path('api/categories/', views.CategoryView.as_view()), 
   path('api/categories/<int:id>/', views.CategoryView.as_view(), name='category-detail'),
   path('api/categories/<int:id>/products/', views.CategoryProductsView.as_view(), name='category-detail'),
   path('api/categories/clear/', ClearCategoriesView.as_view(), name='clear_categories'),
]