# Generated by Django 5.0.2 on 2024-11-02 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0025_remove_product_cut_price_cut_type_and_more'),
        ('weesli_app', '0003_alter_order_product_product_added'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product_cut_price',
        ),
    ]
