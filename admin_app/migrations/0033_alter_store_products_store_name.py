# Generated by Django 5.0.2 on 2024-11-09 13:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0032_alter_store_products_store_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store_products',
            name='store_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.store'),
        ),
    ]
