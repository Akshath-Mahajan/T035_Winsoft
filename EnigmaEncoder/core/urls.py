from django.contrib import admin
from django.urls import path
from .views import home,output

urlpatterns = [
    path('', home.as_view(), name="home"),
    path('output/', output.as_view(), name="output"),
]