from django import forms
from .models import Blog

# class RegistrationForm(forms.Form):
#             num1 = forms.CharField()
#             num2 = forms.CharField()

class BlogForm(forms.ModelForm):
        class Meta:
            model = Blog
            fields = '__all__'