# Generated by Django 5.0.6 on 2024-05-24 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_producttagmodel_productsmodel_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productscategorymodel',
            name='parent',
        ),
    ]