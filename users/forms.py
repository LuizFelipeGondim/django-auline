
from django import forms 
from .models import Perfil
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)

        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ('data_de_nascimento', 'telefone', 'foto', 'cidade_usuario', 'estado_usuario', 'rua_usuario')
        widgets = {
            'data_de_nascimento': forms.DateInput(attrs={'class':'form-control', 'placeholder':'DD/MM/YYYY'}),
            'telefone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'(77)98888-8888'}),
            'foto': forms.TextInput(attrs={'class':'form-control'}),
            'cidade_usuario': forms.TextInput(attrs={'class':'form-control labe', }),
            'estado_usuario': forms.TextInput(attrs={'class':'form-control'}),
            'rua_usuario': forms.TextInput(attrs={'class':'form-control'}),
        }


