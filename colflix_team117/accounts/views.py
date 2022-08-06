from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User, auth
from django.contrib import messages

from django.views import View


class Register(View):
    form_class = RegisterForm
    template_name = 'register.html'
    
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

            #create and user with the inputed credentialsto the db
            user = User.objects.create_user(name=name, username=u_name, password=pswd, email=mail)
            user.save()
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
