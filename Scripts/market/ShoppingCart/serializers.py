from rest_framework import serializers
from .models import Cart, CartItem, Product

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity']

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'created_at', 'updated_at', 'items']
        
class ProductSerializer(serializers.ModelSerializer):  
   class Meta:  
      model = Product  
      fields = ['id', 'name', 'description', 'price', 'image']