from rest_framework import status  
from rest_framework.response import Response  
from rest_framework.views import APIView  
from .serializers import ProductSerializer  
from .models import Product
from django.http import JsonResponse
from django.db import connection
  
class ProductAddGetView(APIView):  
   def get(self, request):  
        products = Product.objects.all()
        
        for product in products:
            product.views += 1
            product.save()

        serializer = ProductSerializer(products, many=True)  
        return Response(serializer.data) 
  
   def post(self, request):  
      serializer = ProductSerializer(data=request.data)  
      if serializer.is_valid():  
        serializer.save()  
        return Response(serializer.data, status=status.HTTP_201_CREATED)  
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
  
class ProductUpdateDeleteView(APIView):  
   def put(self, request, pk):  
      try:  
        product = Product.objects.get(pk=pk)  
      except Product.DoesNotExist:  
        return Response(status=status.HTTP_404_NOT_FOUND)  
  
      serializer = ProductSerializer(product, data=request.data)  
      if serializer.is_valid():  
        serializer.save()  
        return Response(serializer.data, status=status.HTTP_200_OK)  
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
  
   def delete(self, request, pk):  
      try:  
        product = Product.objects.get(pk=pk)  
      except Product.DoesNotExist:  
        return Response(status=status.HTTP_404_NOT_FOUND)  
  
      product.delete()  
      return Response(status=status.HTTP_204_NO_CONTENT)
    
class ClearProductsView(APIView):
    def delete(self, request):
        try:
            Product.objects.all().delete()

            with connection.cursor() as cursor:
                cursor.execute("ALTER TABLE ManagingProducts_Product AUTO_INCREMENT = 1;")
            
            return Response({"message": "All products have been deleted and ID reset."}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
