from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from pdbapp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^item/(?P<item_id>[0-9]+)',views.item, name='item')
]
