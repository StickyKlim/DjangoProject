from django.contrib import admin
from django.urls import path
from djapp import views
from django.conf.urls.static import static
from django.urls.conf import include
from django.conf import settings

urlpatterns = [
    path('', views.index, name='home'),
    path("myform", views.myform),
]