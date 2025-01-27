# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("logout", views.logout_page, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("users/", views.users, name="users"),
    path("user_role/", views.user_role, name="user_role"),
]
