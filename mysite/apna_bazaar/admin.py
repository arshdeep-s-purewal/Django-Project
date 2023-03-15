from django.contrib import admin
from .models import ApnaBazaar

# Register your models here.
class ApnaBazaarAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "quantity"]

admin.site.register(ApnaBazaar, ApnaBazaarAdmin)