from django.shortcuts import render

def main(request):
    return render(request,"layouts/main.html")
def dashboard(request):
    return render(request,"modules/dashboard.html")
def users(request):
    return render(request,"modules/masters/users.html")
def user_role(request):
    return render(request,"modules//masters/user_role.html")