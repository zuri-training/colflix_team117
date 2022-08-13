from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Video
from .serializers import VideoSerializer
from rest_framework import generics


class LandingPageView(TemplateView):
    template_name = 'landing_page.html' 
    
class HomePageView(TemplateView): 
    template_name = 'index.html' 
    queryset = Video.objects.order_by('-published')
    context_object_name = 'video_list'
    
class PostVideo(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer