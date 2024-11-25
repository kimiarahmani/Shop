from django.urls import path
from .views import AddToCartView, RemoveFromCartView, GetCartView, ClearCartView

urlpatterns = [
    path('api/cart/add/<int:product_id>/', AddToCartView.as_view(), name='add_to_cart'),
    path('api/cart/remove/<int:product_id>/', RemoveFromCartView.as_view(), name='remove_from_cart'),
    path('api/cart/', GetCartView.as_view(), name='get_cart'),
    path('api/cart/clear/', ClearCartView.as_view(), name='clear_cart'),
]