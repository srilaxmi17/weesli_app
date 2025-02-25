# Generated by Django 5.0.2 on 2024-11-02 07:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0024_store_store_description_alter_store_store_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_cut_price',
            name='cut_type',
        ),
        migrations.RemoveField(
            model_name='product_cut_price',
            name='product_name',
        ),
        migrations.RemoveField(
            model_name='product_type',
            name='product_type_image',
        ),
        migrations.RemoveField(
            model_name='store',
            name='bussiness_hour',
        ),
        migrations.AddField(
            model_name='today_catch',
            name='store_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='admin_app.store'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='today_catch',
            name='t_product_available_quantity',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.CreateModel(
            name='Store_products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('mrp', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('product_image', models.ImageField(upload_to='product_image/')),
                ('product_available_quantity', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.category')),
                ('cut_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.cut_type')),
                ('store_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.store')),
            ],
        ),
        migrations.AlterField(
            model_name='today_catch',
            name='product_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.store_products'),
        ),
        migrations.DeleteModel(
            name='Product_name',
        ),
    ]
