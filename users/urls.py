from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect
from users.views import home_view 
from .views import register_view,live_view
from django.urls import path, include
from . import views

def user_list(request):
    return HttpResponse("List of Users")

def user_detail(request, user_id):
    return HttpResponse(f"Details for User ID: {user_id}")



urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),

    path('live/', views.live_view, name='live'),  # Live match page
    path('', user_list, name='user_list'),
    path('<int:user_id>/', user_detail, name='user_detail'),
]

