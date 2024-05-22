# Generated by Django 5.0.6 on 2024-05-24 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_productcategorymodel_producttocategory_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producttocategory',
            name='category',
        ),
        migrations.RemoveField(
            model_name='producttocategory',
            name='product',
        ),
        migrations.AlterField(
            model_name='productsmodel',
            name='categories',
            field=models.ManyToManyField(related_name='categories', to='products.productscategorymodel'),
        ),
        migrations.DeleteModel(
            name='ProductCategoryModel',
        ),
        migrations.DeleteModel(
            name='ProductToCategory',
        ),
    ]