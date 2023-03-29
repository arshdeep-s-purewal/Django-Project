from django.db import models
from django.contrib.auth.models import User
# from myapp.models import Contact

# Create your models here.
class ApnaBazaar(models.Model):
    name = models.CharField(max_length=150)
    price = models.CharField(max_length=150)
    quantity = models.IntegerField()
    product_image = models.ImageField(upload_to='images/', null=True)
    category = models.CharField(max_length = 200)
    product_description = models.TextField(max_length= 2000)

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(ApnaBazaar, on_delete=models.CASCADE)


class Address(models.Model):
    name = models.CharField(max_length=200)
    mobile_no = models.CharField(max_length=10)
    pin_code = models.CharField(max_length=15)
    address = models.CharField(max_length=300)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    ordered_at = models.DateTimeField(auto_now=True)
    total = models.CharField(max_length=10000000)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(ApnaBazaar, on_delete=models.CASCADE)
    price = models.CharField(max_length=1000000)

