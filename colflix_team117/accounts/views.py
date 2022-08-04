from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User, auth
from django.contrib import messages


#NOTE user authentication not yet completed...password not checked
def register(request):
    if request.method == "POST":
        reg_form = RegisterForm(request.POST)

        if reg_form.is_valid():
            name = reg_form.cleaned_data["name"]
            u_name = reg_form.cleaned_data["username"]
            mail = reg_form.cleaned_data["email"]
            pswd = reg_form.cleaned_data["password"]

            user = User.objects.create_user(name=name, username=u_name, password=pswd, email=mail)
            user.save()
            return redirect("/")
    # if a GET (or any other method) we'll create a blank form and render to the page
    reg_form = RegisterForm()
    return render(request, 'register.html', {'reg_form':reg_form})


def login(request):
    if request.method == 'POST':
        log_form = LoginForm(request.POST)

        #Note cleaned_data is only available when you use is_valid
        if log_form.is_valid():
            u_name = log_form.cleaned_data["username"]
            pswd = log_form.cleaned_data["password"]

            #check if user in database
            user = auth.authenticate(username=u_name, password=pswd)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'wrong username or password')
            return redirect('login')

    log_form = LoginForm()
    return render(request, 'login.html', {'log_form':log_form})


def logout_req(request):
    auth.logout(request)
    return redirect('/')
