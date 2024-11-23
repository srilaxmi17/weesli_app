from rest_framework import serializers
from admin_app.models import *


class todayscatchSerializer(serializers.ModelSerializer):
    category_name=serializers.CharField(source='product_name.category.category')
    product_image=serializers.CharField(source='product_name.product_image')
    mrp=serializers.CharField(source='product_name.mrp')
    product_name=serializers.CharField(source='product_name.product_name')

    class Meta:
        model = Store_product_cutPrice
        fields = ['product_image','mrp','category_name','product_name','product_price']

class categorySerializer(serializers.ModelSerializer):
    product_image=serializers.CharField(source='product_name.product_image')
    product_name=serializers.CharField(source='product_name.product_name')

    class Meta:
        model = Store_product_cutPrice
        fields = ['product_image','product_name','product_price']

class categoryname_displaySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['category','category_image']

class categorynameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['category']