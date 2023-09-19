
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('', views.f1),
    path('new/',views.f2),
]
