from django.urls import path
from weesli_app.views import *

urlpatterns = [
    path('todaycatch/',todaycatch.as_view(),name='todaycatch'),
    path('product/<int:id>/',product_type.as_view(),name='product'),
    path('product/<int:product_id>/category/<int:category_id>/',category_product.as_view(),name='product'),
    path('category_list/',categoryname_display.as_view(),name='categoryname_display'),
    path('categoryname/<int:productid>/',categoryname.as_view(),name='categoryname'),
           
]