from django import forms
from .models import ApnaBazaar, Address
from django.contrib.auth.models import User

class ApnaBazaarForm(forms.ModelForm):
    class Meta:
        model = ApnaBazaar
        fields = '__all__'

class CreateNewUserForm(forms.ModelForm):
      class Meta:
            model = User
            fields = ('username','password','email')

class AddAddressForm(forms.ModelForm):
     class Meta:
          model = Address
          fields = '__all__'