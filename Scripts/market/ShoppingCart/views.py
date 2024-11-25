from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Cart, CartItem
from categories.models import Product
from .serializers import CartSerializer, ProductSerializer

class AddToCartView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)

        cart, created = Cart.objects.get_or_create(user=request.user)

        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

        if not created:
            cart_item.quantity += 1
            cart_item.save()

        cart_serializer = CartSerializer(cart)
        return Response(cart_serializer.data, status=status.HTTP_201_CREATED)

class RemoveFromCartView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, product_id):
        try:
            cart = Cart.objects.get(user=request.user)  
            cart_item = CartItem.objects.get(cart=cart, product_id=product_id)
            cart_item.delete()
            return Response({'message': 'Product removed from cart successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Cart.DoesNotExist:
            return Response({'error': 'Cart not found'}, status=status.HTTP_404_NOT_FOUND)
        except CartItem.DoesNotExist:
            return Response({'error': 'Product not found in cart'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class GetCartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            cart = Cart.objects.get(user=request.user) 
            cart_items = CartItem.objects.filter(cart=cart)  
            
            products = [item.product for item in cart_items]
            serializer = ProductSerializer(products, many=True)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Cart.DoesNotExist:
            return Response({'error': 'Cart not found'}, status=status.HTTP_404_NOT_FOUND)
        
class ClearCartView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        try:
            cart = Cart.objects.get(user=request.user)
            cart.items.all().delete()
            return Response({'message': 'All products removed from cart successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Cart.DoesNotExist:
            return Response({'error': 'Cart not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

