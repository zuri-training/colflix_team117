from django import forms
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User



class RegisterForm(UserCreationForm):
    name = forms.CharField(label="First Name", max_length=200)
    email = forms.EmailField(label="Email", max_length=200)
    
    class Meta:  
        model = User  
        fields = ('name', 'email', 'username', 'password1')  

class LoginForm(forms.Form):
    username = forms.CharField(label="Userame", max_length=200)
    password= forms.CharField(label="Password", max_length=200)