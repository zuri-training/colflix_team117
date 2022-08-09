from django.urls import path
from .views import HomePageView, Activate


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('activate', Activate.as_view(), name='activate'),
]