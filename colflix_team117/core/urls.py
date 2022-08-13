from django.urls import path
from .views import HomePageView, LandingPageView, PostVideo


urlpatterns = [
    path('', LandingPageView.as_view(), name='landing-page'),
    path('index', HomePageView.as_view(), name='index'),
    path('post-video', PostVideo.as_view(), name='post-video')
]