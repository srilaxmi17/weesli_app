from django.shortcuts import render
from weesli_app.serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from admin_app.models import *
from rest_framework.generics import ListAPIView,RetrieveAPIView

class todaycatch(ListAPIView):
    serializer_class=todayscatchSerializer
    products=Store_products.objects.filter(is_available=True,is_todays_catch=True)
    queryset=Store_product_cutPrice.objects.filter(product_name__in=products,is_default_cutprice=True)


class product_type(ListAPIView):
    serializer_class=categorySerializer

    def get_queryset(self):
        product_id=self.kwargs.get('id')
        product=Store_products.objects.filter(is_available=True,category__in=Category.objects.filter(product_type_id=product_id))
        return Store_product_cutPrice.objects.filter(product_name__in=product,is_default_cutprice=True)


class category_product(ListAPIView):
    serializer_class=categorySerializer

    def get_queryset(self):
        product_id=self.kwargs.get('product_id')
        category_id=self.kwargs.get('category_id')
        product=Store_products.objects.filter(is_available=True,category__in=Category.objects.filter(product_type_id=product_id))
        product=product.filter(category_id=category_id)
        return Store_product_cutPrice.objects.filter(product_name__in=product,is_default_cutprice=True)
        

class categoryname_display(ListAPIView):
    serializer_class=categoryname_displaySerializer
    queryset= Category.objects.all()

class categoryname(ListAPIView):
    serializer_class=categorynameSerializer

    def get_queryset(self):
        productid=self.kwargs.get('productid')
        return Category.objects.filter(product_type_id=productid)

