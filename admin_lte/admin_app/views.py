from django.shortcuts import render
from .models import UserRole

# def main(request):
#     return render(request,"layouts/main.html")
def dashboard(request):
    return render(request,"modules/dashboard.html")
def users(request):
    return render(request,"modules/masters/users.html")
def user_role(request):
    user_roles = UserRole.objects.all()
    context = {
        'page_title': "User Roles",
        'user_roles': user_roles,
    }    
    return render(request,"modules//masters/user_role.html",context)