import csv
from django.core.management.base import BaseCommand
from ManagingProducts.models import Product

class Command(BaseCommand):
    help = 'Generate CSV of products sorted by views'

    def handle(self, *args, **kwargs):
        products = Product.objects.all().order_by('-views')
        with open('products.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['views', 'product', 'category'])
            for product in products:
                writer.writerow([product.views, product.name, product.category.name])
        self.stdout.write(self.style.SUCCESS('Successfully generated products.csv'))