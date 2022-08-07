from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views
from .forms import PwdChangeForm, PwdResetForm, UserLoginForm, PwdResetConfirmForm

app_name='accounts'

urlpatterns = [
    path('landing/', views.index, name='landingpage'),
    path('login/', auth_views.LoginView.as_view(template_name="registration/login.html", authentication_form=UserLoginForm), name='login'),
]