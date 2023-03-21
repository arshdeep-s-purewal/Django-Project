from django import forms
from .models import ApnaBazaar
from django.contrib.auth.models import User

class ApnaBazaarForm(forms.ModelForm):
    class Meta:
        model = ApnaBazaar
        fields = '__all__'

class CreateNewUserForm(forms.ModelForm):
      class Meta:
            model = User
            fields = ('username','password','email')