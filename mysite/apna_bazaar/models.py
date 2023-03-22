from django.db import models

# Create your models here.
class ApnaBazaar(models.Model):
    name = models.CharField(max_length=150)
    price = models.CharField(max_length=150)
    quantity = models.CharField(max_length=150)
    product_image = models.ImageField(upload_to='images/')


    
