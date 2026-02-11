from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name = 'register'),
    path('login', views.loginReq, name = 'login'),
    path('logout', views.logoutReq, name = 'logout')]