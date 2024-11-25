from django.db import models  

class Category(models.Model):  
   name = models.CharField(max_length=255)  
   description = models.TextField(blank=True)
  
   def delete(self, *args, **kwargs):  
      super().delete(*args, **kwargs)
      
class Product(models.Model):  
    name = models.CharField(max_length=255)  
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=10)  
    image = models.ImageField(upload_to='products/', blank=True) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):  
        return self.name