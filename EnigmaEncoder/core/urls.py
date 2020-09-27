from django.contrib import admin
from django.urls import path
from .views import home,output,login, logout
urlpatterns = [
    path('', home.as_view(), name="home"),
    path('output/', output.as_view(), name="output"),
    path('login/', login.as_view(), name="login"),
    path('logout/', logout.as_view(), name="logout"),
]