# Generated by Django 3.1 on 2020-08-12 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_test', '0002_product_prod_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='prod_desc',
            new_name='product_desc',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='prod_image',
            new_name='product_image',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='prod_price',
            new_name='product_price',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='prod_title',
            new_name='product_title',
        ),
    ]