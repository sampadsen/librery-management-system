from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.login,name="login"),
    path('collect',views.collect,name="collect")
]