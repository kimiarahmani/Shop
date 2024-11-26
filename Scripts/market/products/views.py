from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import random  
from categories.models import Category, Product

def home(request):  
   return render(request, 'home.html')  
  
def electronics(request):  
   return render(request, 'electronics.html')  
  
def clothing(request):  
   return render(request, 'clothing.html')  
  
def home_goods(request):  
   return render(request, 'home_goods.html')  
  
def beauty(request):  
   return render(request, 'beauty_products.html')
  