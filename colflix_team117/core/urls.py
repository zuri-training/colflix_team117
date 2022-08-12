from django.urls import path
from .views import HomePageView, LandingPageView


urlpatterns = [
    path('', LandingPageView.as_view(), name='landing-page'),
    path('index', HomePageView.as_view(), name='index'),
]