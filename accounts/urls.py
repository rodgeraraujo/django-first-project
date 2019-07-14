"""accounts URL Configuration
"""
from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'login/', views.login, name='login'),
    path(r'register/', views.register, name='register')
]
