from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.views import View


class Register(View):
    form_class = RegisterForm
    template_name = 'register.html'
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, 'register.html', {'form':form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        #Note cleaned_data is only available when you use is_valid
        if form.is_valid():
            name = form.cleaned_data["name"]
            u_name = form.cleaned_data["username"]
            mail = form.cleaned_data["email"]
            pswd = form.cleaned_data["password"]

            user = User.objects.create_user(first_name=name, username=u_name, password=pswd, email=mail)
            user.save()
            return redirect('/')

class Login(View):
    form_class = LoginForm
    template_name = 'login.html'
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, 'login.html', {'form':form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            u_name = form.cleaned_data["username"]
            pswd = form.cleaned_data["password"]
            #check if user in database
            user = auth.authenticate(username=u_name, password=pswd)
        elif user is not None:
            auth.login(request, user)
            return redirect('/') #redirect to root/home page
        else:
            messages.info(request, 'wrong username or password')
            return redirect('login') #back to login page if input is wrong

def logout_req(request):
    auth.logout(request)
    return redirect('/')
