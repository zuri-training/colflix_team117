from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView): 
    template_name = 'index.html' # 
    
class LandingPageView(TemplateView):
    template_name = 'landing_page.html' #
