from django.db import models
from django.contrib.auth.hashers import make_password,check_password

# Create your models here.

class Admin_login(models.Model):
    admin_name=models.CharField(max_length=30)
    admin_mail=models.EmailField(unique=True)
    admin_password=models.CharField(max_length=30)

    def __str__(self):
        return self.admin_name
    
    def hash_password(self,admin_password):
        self.admin_password=make_password(admin_password)

    def check_password(self,admin_password):
        return check_password(admin_password,self.admin_password)    

class Store_owner_login(models.Model):
    store_ownwer_name=models.CharField(max_length=200)
    store_ownwer_email=models.EmailField(unique=True)
    store_ownwer_password=models.CharField(max_length=200)
    store_ownwer_mobile=models.IntegerField()
    # owner_is_active=models.BooleanField(default=True)
    owner_is_suspicious=models.BooleanField(default=False)

    def __str__(self):
        return self.store_ownwer_name

    def hash_password(self,store_ownwer_password):
        self.store_ownwer_password=make_password(store_ownwer_password)

    def check_password(self,store_ownwer_password):
        return check_password(store_ownwer_password,self.store_ownwer_password)

class State(models.Model):
    state=models.CharField(max_length=100)

    def __str__(self):
        return self.state
    
class City(models.Model):
    state=models.ForeignKey(State,on_delete=models.CASCADE)
    city=models.CharField(max_length=100)

    def __str__(self):
        return self.city    

class Store(models.Model):
    store_ownwer_name=models.ForeignKey(Store_owner_login,on_delete=models.CASCADE)
    store_name=models.TextField(max_length=200)
    store_location=models.TextField(max_length=200)
    store_description = models.TextField(blank=True, null=True)
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    zip_code = models.CharField(max_length=20)
    latitude= models.DecimalField(max_digits=9,decimal_places=6)
    longitude= models.DecimalField(max_digits=9,decimal_places=6)
    store_number=models.IntegerField(blank=True,null=True)
    store_image = models.ImageField(upload_to='store_images/', blank=True, null=True)
    store_is_active=models.BooleanField(default=True)
    store_is_suspicious=models.BooleanField(default=False)

    def __str__(self):
        return self.store_name


class Product_Type(models.Model):
    product_type=models.CharField(max_length=200)

    def __str__(self):
        return self.product_type

class Cut_type(models.Model):
    cut_type=models.CharField(max_length=200)
    cut_image=models.ImageField(upload_to='cut_image/')
    
    def __str__(self):
        return self.cut_type 

class Category(models.Model):
    product_type=models.ForeignKey(Product_Type,on_delete=models.CASCADE)
    category=models.CharField(max_length=200)
    category_image=models.ImageField(upload_to='category_image/')
   
    def __str__(self):
        return self.category

class Store_products(models.Model):
    store_name=models.ForeignKey(Store,on_delete=models.CASCADE)
    product_name=models.CharField(max_length=200)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    mrp=models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    product_image=models.ImageField(upload_to='product_image/')
    product_available_quantity=models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    is_todays_catch=models.BooleanField(default=False)
    is_available=models.BooleanField(default=False)
    
    def __str__(self):
        return self.store_name.store_name

class Store_product_cutPrice(models.Model):
    product_name=models.ForeignKey(Store_products,on_delete=models.CASCADE)
    cut_type=models.ForeignKey(Cut_type,on_delete=models.CASCADE)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_default_cutprice=models.BooleanField(default=False)

    def __str__(self):
        return self.product_name.product_name

