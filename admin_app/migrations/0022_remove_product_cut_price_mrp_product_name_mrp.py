# Generated by Django 5.0.2 on 2024-10-29 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0021_remove_store_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_cut_price',
            name='mrp',
        ),
        migrations.AddField(
            model_name='product_name',
            name='mrp',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
