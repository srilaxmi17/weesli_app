# Generated by Django 5.0.2 on 2024-11-06 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0030_alter_store_product_cutprice_is_todays_catch'),
    ]

    operations = [
        migrations.AddField(
            model_name='store_product_cutprice',
            name='is_available',
            field=models.BooleanField(default=False),
        ),
    ]
