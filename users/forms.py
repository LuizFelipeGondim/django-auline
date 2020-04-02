from django.forms import ModelForm
from django import forms 
from django.contrib.auth.models import User

class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'last_name', 'first_name']
        widgets = {
            'last_name': forms.TextInput(attrs={'class':'form-control', 'max-length': 100}),
            'first_name': forms.TextInput(attrs={'class':'form-control', 'max-length': 100}),
            'password': forms.PasswordInput(attrs={'class':'form-control', 'max-length': 30}),
            'email': forms.TextInput(attrs={'class':'form-control', 'max-length': 100}),
            'username': forms.TextInput(attrs={'class':'form-control', 'max-length': 100}),
        }
