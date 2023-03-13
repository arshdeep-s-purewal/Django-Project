from django import forms
from .models import ApnaBazaar

class ApnaBazaarForm(forms.ModelForm):
    class Meta:
        model = ApnaBazaar
        fields = '__all__'