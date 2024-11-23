# Generated by Django 5.0.2 on 2024-11-07 08:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0031_store_product_cutprice_is_available'),
        ('weesli_app', '0003_alter_order_product_product_added'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_id', models.CharField(blank=True, max_length=100, null=True)),
                ('quantity_choosen', models.DecimalField(decimal_places=2, max_digits=5)),
                ('total_sum', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_mode', models.CharField(max_length=100)),
                ('delivery_slot_date', models.DateTimeField()),
                ('user_location', models.CharField(max_length=200)),
                ('payment_id', models.CharField(blank=True, max_length=100, null=True)),
                ('order_id', models.CharField(blank=True, max_length=100, null=True)),
                ('payment_status', models.CharField(default='Pending', max_length=50)),
                ('cart_created_at', models.DateTimeField(auto_now=True)),
                ('delivery_slot_time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weesli_app.delivery_slot_time')),
                ('product_added', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.store_products')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='weesli_app.user')),
            ],
        ),
        migrations.CreateModel(
            name='UserOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_mode', models.CharField(max_length=100)),
                ('delivery_slot_date', models.DateTimeField()),
                ('user_location', models.CharField(max_length=200)),
                ('payment_id', models.CharField(blank=True, max_length=100, null=True)),
                ('order_id', models.CharField(blank=True, max_length=100, null=True)),
                ('payment_status', models.CharField(default='Pending', max_length=50)),
                ('order_created_at', models.DateTimeField(auto_now=True)),
                ('cart_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weesli_app.usercart')),
                ('delivery_slot_time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weesli_app.delivery_slot_time')),
            ],
        ),
        migrations.DeleteModel(
            name='Order_product',
        ),
    ]
