# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("logout", views.logout_page, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    
    path("state/", views.state, name="state"),
    path("state/create", views.state_create, name="state_create"),
    path("state/store", views.add_state, name="add-state"),
    path("state/edit/<int:state_id>/", views.state_edit, name="state_edit"),
    path("state/update/<int:state_id>", views.state_update, name="state_update"),
    path("state/delete/<int:state_id>/", views.state_delete, name="state_delete"),
    
    path("users/", views.users, name="users"),
    path("user_role/", views.user_role, name="user_role"),
]
