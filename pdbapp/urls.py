from django.contrib import admin
from django.urls import path

from pdbapp import views

urlpatterns = [
    path('', views.index, name='index'),
]
