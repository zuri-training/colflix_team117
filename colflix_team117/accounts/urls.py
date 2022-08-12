from django.urls import path
from . import views

from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView

urlpatterns = [
    path('sign-up', views.SignUp.as_view(), name='sign-up'),
    path('sign-in', views.SignIn.as_view(), name='sign-in'),
    path('logout_req', views.logout_req, name='logout_req'),
    #path('secret', login_required(TemplateView.as_view(template_name="secret.html")), name="secret"),
]

