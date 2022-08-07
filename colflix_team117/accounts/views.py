from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.views import View
from django.core.mail import send_mail

import math, random

#user gets page
#user posts details
    #two validations 
        #is the form valid
        #is the email valid
#if .edu in mail
    #generate OTP
    #send a mail
#redirect to OTP page
#if user enters the write OTP
    #create and save user

class Register(View):
    form_class = RegisterForm
    template_name = 'register.html'
    
    def generateOTP(self):
        digits = "0123456789"
        OTP = ""
        for i in range(6):
            #random return decimals in range 0 t0 1, *10 and math.floor changes the return number to a whole number
            OTP += digits[math.floor(random.random() * 10)]
        return OTP
    
    def get(self, request, *args, **kwargs):
        # if a GET it will create a blank form and render to the page
        reg_form = self.form_class()
        return render(request, 'register.html', {'reg_form':reg_form})
    
    def post(self, request, *args, **kwargs):
        reg_form = self.form_class(request.POST)
        #Note cleaned_data is only available when you use is_valid
        if reg_form.is_valid():
            name = reg_form.cleaned_data["name"]
            u_name = reg_form.cleaned_data["username"]
            mail = reg_form.cleaned_data["email"]
            pswd = reg_form.cleaned_data["password"]

            if ".com" in mail:
                OTP = self.generateOTP()
                send_mail(
                    'Enter the OTP below to confirm your mail',
                    OTP,
                    'josephbusayojayeoba@gmail.com',
                    [mail],
                    fail_silently=False,
                )
                #create and user with the inputed credentialsto the db
                user = User.objects.create_user(name=name, username=u_name, password=pswd, email=mail)
                #user.save()
                return redirect("/")

class Login(View):
    form_class = LoginForm
    template_name = 'login.html'
    
    def get(self, request, *args, **kwargs):
        log_form = LoginForm()
        return render(request, 'login.html', {'log_form':log_form})
    
    def post(self, request, *args, **kwargs):
        log_form = LoginForm(request.POST)
        if log_form.is_valid():
            u_name = log_form.cleaned_data["username"]
            pswd = log_form.cleaned_data["password"]
            #check if user in database
            user = auth.authenticate(username=u_name, password=pswd)
            
        #if user does exists
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'wrong username or password')
            return redirect('login')
        
def logout_req(request):
    auth.logout(request)
    return redirect('/')
