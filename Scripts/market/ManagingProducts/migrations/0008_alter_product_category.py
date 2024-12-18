# Generated by Django 5.1.3 on 2024-11-23 21:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManagingProducts', '0007_alter_product_price'),
        ('categories', '0006_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='categories.category'),
        ),
    ]
