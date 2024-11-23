from django.contrib import admin
from admin_app.models import *

# Register your models here.Product_Type

class StoreProductCutPriceInline(admin.TabularInline):
    model = Store_product_cutPrice

class StoreProductsAdmin(admin.ModelAdmin):
    inlines = [StoreProductCutPriceInline]    

admin.site.register(Admin_login)
admin.site.register(Store_owner_login)
admin.site.register(Store)
admin.site.register(Product_Type)
admin.site.register(Cut_type)
admin.site.register(Category)
admin.site.register(Store_products,StoreProductsAdmin)
admin.site.register(State)
# admin.site.register(Store_products)
admin.site.register(Store_product_cutPrice)
admin.site.register(City)