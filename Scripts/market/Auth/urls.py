from django.urls import path  
from . import views
from .views import LogoutView
  
urlpatterns = [  
   path('api/auth/token/', views.ObtainTokenView.as_view(), name='obtain_token'),  
   path('api/auth/token/refresh/', views.RefreshTokenView.as_view(), name='refresh_token'),  
   path('api/auth/token/logout/', LogoutView.as_view(), name='logout'),
]