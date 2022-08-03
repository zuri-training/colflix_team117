from django.shortcuts import render
from django.views.generic import ListView


class HomePageView(ListView):
    template_name = 'index.html' # homepage

class LandingPageView(ListView):
    template_name = 'landing-page.html' #landing-page
