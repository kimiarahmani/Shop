from django.contrib.auth.models import User
from django.db import models

class Product(models.Model):  
   name = models.CharField(max_length=255)  
   description = models.TextField(blank=True)  
   price = models.DecimalField(max_digits=10, decimal_places=2, null=True)  
   image = models.ImageField(upload_to='products/', blank=True) 
   
   def __str__(self):  
      return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='1')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart {self.id} for {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey('categories.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"
