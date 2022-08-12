from django.urls import path
from .views import HomePageView, LandingPageView


urlpatterns = [
    path('index', HomePageView.as_view(), name='home'),
    path('landing-page', LandingPageView.as_view(), name='activate'),
]