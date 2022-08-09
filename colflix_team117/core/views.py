from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
<<<<<<< HEAD
    template_name = 'landing_page.html' 
=======
    template_name = 'index.html' # 
    
class Activate(TemplateView):
    template_name = 'activate.html' #
>>>>>>> main
