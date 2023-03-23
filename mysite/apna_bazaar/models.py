from django.db import models
from django.views.generic import ListView
# from myapp.models import Contact

# Create your models here.
class ApnaBazaar(models.Model):
    name = models.CharField(max_length=150)
    price = models.CharField(max_length=150)
    quantity = models.IntegerField()
    product_image = models.ImageField(upload_to='images/')
    category = models.CharField(max_length = 200)
    product_description = models.TextField(max_length= 2000)


# class ContactListView(ListView):
#     paginate_by = 2
#     model = Contact

class Wishlist(models.Model):
    pass


    
