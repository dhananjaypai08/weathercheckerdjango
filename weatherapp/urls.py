from django.contrib import admin
from django.urls import path, include
from weatherapp import views

urlpatterns = [
    path('', views.home, name='home'),
]