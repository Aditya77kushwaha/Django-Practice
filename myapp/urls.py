from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('show/', views.show),
    path('form/', views.form),
    path('form1/', views.form)
]
