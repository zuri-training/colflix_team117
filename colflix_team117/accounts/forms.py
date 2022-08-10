from tkinter import Widget
from django import forms
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User



class RegisterForm(UserCreationForm):
    name = forms.CharField(label="First Name", max_length=200)
    email = forms.EmailField(label="Email", max_length=200)
<<<<<<< HEAD
    
=======
>>>>>>> main
    class Meta:  
        model = User  
        fields = ('name', 'email', 'username', 'password1')  


class LoginForm(forms.Form):
    username = forms.CharField(label="Username/email",
    max_length=200)
    password= forms.CharField(label="Password",max_length=200)

    username.widget.attrs.update({'class': 'form-control'})
    password.widget.attrs.update({'class':'form-control'})

"""
=======
    username = forms.CharField(label="Username", max_length=200)
    password= forms.CharField(label="Password", max_length=200)
    
    name.widget.attrs.update({'class': 'form-control'})
    email.widget.attrs.update({'class':'form-control'})
    username.widget.attrs.update({'class': 'form-control'})
    password.widget.attrs.update({'class':'form-control'})
"""