from django.db import models
from categories.models import Category
  
class Product(models.Model):  
    name = models.CharField(max_length=255)  
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=10)  
    image = models.ImageField(upload_to='products/', blank=True) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    views = models.IntegerField(default=0)

    def __str__(self):  
        return self.name
