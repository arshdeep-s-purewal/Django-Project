from django.contrib import admin
from .models import ApnaBazaar

# Register your models here.
class ApnaBazaarAdmin(admin.ModelAdmin):
    list_display = ["Name", "Price", "Quantity"]

admin.site.register(ApnaBazaar, ApnaBazaarAdmin)