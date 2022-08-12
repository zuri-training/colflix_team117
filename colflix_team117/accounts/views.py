from django.shortcuts import render, redirect, HttpResponse
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.views import View
from django.core.mail import EmailMessage

from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site  
from django.utils.encoding import force_bytes, force_str  
from django.template.loader import render_to_string  
from django.contrib.auth.tokens import PasswordResetTokenGenerator  
from six import text_type  



class TokenGenerator(PasswordResetTokenGenerator):  
    def _make_hash_value(self, user, timestamp):  
        return (  
            text_type(user.pk) + text_type(timestamp) + text_type(user.is_active)  
        )  
        
class SignUp(View):
    form_class = RegisterForm
    template_name = 'register.html'
    account_activation_token = TokenGenerator() 
    
    def get(self, request, *args, **kwargs):#if a GET it will create a blank form and render to the page
        form = self.form_class()
        return render(request, 'register.html', {'form':form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid(): #Note cleaned_data is only available when you use is_valid
            # save form in the memory not in database  
            user = form.save(commit=False)  
            user.is_active = False  
            user.save() 
            
            mail = form.cleaned_data["email"]
            current_site = get_current_site(request)
            message = render_to_string('activate.html', {
                'user': user,
                'doamin': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':self.account_activation_token.make_token(user),
            })
            
            email = EmailMessage(
                'Colflix user account activation link', #mail subject
                message,
                to = [mail],
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')  
        return redirect('register')
"""
#create and user with the inputed credentialsto the db
                user = User.objects.create_user(name=name, username=u_name, password=pswd, email=mail)
                #user.save()
"""

class SignIn(View):
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

