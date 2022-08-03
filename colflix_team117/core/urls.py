from django.urls import path
from .views import HomePageView, LandingPageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'), # home page
    path('\landing-page', LandingPageView.as_view(), name='landing-page'), # landing page
]