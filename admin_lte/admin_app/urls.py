# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path("", views.main, name="main"),
    path("", views.dashboard, name="dashboard"),  
    path("users/", views.users, name="users"),  
    path("user_role/", views.user_role, name="user_role"),  
]
