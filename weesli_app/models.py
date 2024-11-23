from django.db import models
from admin_app.models import *

# Create your models here.

class User(models.Model):
    username=models.CharField(max_length=200)
    user_email=models.EmailField(unique=True)
    user_mobile_number=models.IntegerField()
    user_address=models.TextField(max_length=200)

    def __str__(self):
        return self.username

class Delivery_Slot_Time(models.Model):
    delivery_slot_time=models.CharField(max_length=100)

class UserCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    u_id=models.CharField(max_length=100,null=True,blank=True)
    product_added=models.ForeignKey(Store_products,on_delete=models.CASCADE)
    quantity_choosen=models.DecimalField(max_digits=5,decimal_places=2)
    total_sum=models.DecimalField(max_digits=10,decimal_places=2)  
    payment_mode=models.CharField(max_length=100)
    delivery_slot_date=models.DateTimeField()  
    delivery_slot_time=models.ForeignKey(Delivery_Slot_Time,on_delete=models.CASCADE)
    user_location=models.CharField(max_length=200)
    payment_id = models.CharField(max_length=100, null=True, blank=True)  # Razorpay Payment ID
    order_id = models.CharField(max_length=100, null=True, blank=True)  # Razorpay Order ID
    payment_status = models.CharField(max_length=50, default='Pending')
    cart_created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
    
class UserOrders(models.Model):
    cart_details=models.ForeignKey(UserCart,on_delete=models.CASCADE)
    payment_mode=models.CharField(max_length=100)
    delivery_slot_date=models.DateTimeField()  
    delivery_slot_time=models.ForeignKey(Delivery_Slot_Time,on_delete=models.CASCADE)
    user_location=models.CharField(max_length=200)
    payment_id = models.CharField(max_length=100, null=True, blank=True)  # Razorpay Payment ID
    order_id = models.CharField(max_length=100, null=True, blank=True)  # Razorpay Order ID
    payment_status = models.CharField(max_length=50, default='Pending')    
    order_created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cart_details.user.username