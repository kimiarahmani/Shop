# Generated by Django 5.1.3 on 2024-11-23 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManagingProducts', '0006_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=10, max_digits=10),
        ),
    ]
