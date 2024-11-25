from rest_framework import status  
from rest_framework.response import Response  
from rest_framework.views import APIView  
from .models import Category  
from .serializers import CategorySerializer, ProductSerializer
from django.http import JsonResponse
from django.views import View

  
class CategoryView(APIView):  
   def get(self, request):  
      categories = Category.objects.all()  
      serializer = CategorySerializer(categories, many=True)  
      return Response(serializer.data)
    
   def post(self, request):  
      serializer = CategorySerializer(data=request.data)  
      if serializer.is_valid():  
        category = serializer.save()  
        return Response(serializer.data, status=201)  
      return Response(serializer.errors, status=400)
   
   def put(self, request, id):  
      try:  
        category = Category.objects.get(id=id)  
      except Category.DoesNotExist:  
        return Response({"error": "Category not found"}, status=404)  
  
      serializer = CategorySerializer(category, data=request.data, partial=True)  
      if serializer.is_valid():  
        serializer.save()  
        return Response(serializer.data)  
      return Response(serializer.errors, status=400)
   
   def delete(self, request, id):  
      try:  
        category = Category.objects.get(id=id)  
      except Category.DoesNotExist:  
        return Response({"error": "Category not found"}, status=404)  
  
      if category.products.exists():  
        return Response({"error": "Category is being used by a product"}, status=409)  
  
      category.delete()  
      return Response({"message": "Category deleted successfully"}, status=204)
    
   
class CategoryProductsView(APIView):  
   def get(self, request, id):  
      try:  
        category = Category.objects.get(id=id)  
      except Category.DoesNotExist:  
        return Response({"error": "Category not found"}, status=404) 
       
      products = category.products.all()  
      serializer = ProductSerializer(products, many=True)  
      return Response({"products": serializer.data})
   
   def post(self, request, id):  
      try:  
        category = Category.objects.get(id=id)  
      except Category.DoesNotExist:  
        return Response({"error": "Category not found"}, status=404)  
  
      serializer = ProductSerializer(data=request.data)  
      if serializer.is_valid():  
        product = serializer.save(category=category)  
        return Response(serializer.data, status=201)  
      return Response(serializer.errors, status=400)
    

class ClearCategoriesView(View):
    def post(self, request):
        Category.objects.all().delete()

        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("ALTER TABLE categories_category AUTO_INCREMENT = 1;")

        return JsonResponse({'message': 'All categories have been deleted and IDs reset to start from 1.'})
