from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render,redirect
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json



# def main(request):
#     return render(request,"layouts/main.html")
def dashboard(request):
    return render(request,"modules/dashboard.html")

# def login(request):
#     return render(request,"modules/login.html")

@csrf_exempt
def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Parse the AJAX JSON body
            email = data.get('email')
            password = data.get('password')

            user = CustomUser.objects.get(email=email)
            if user and user.password == password:
                login(request, user)
                return JsonResponse({'success': True}, status=200)
            else:
                return JsonResponse({'success': False, 'error': 'Invalid email or password'}, status=422)

        except CustomUser.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Invalid email or password'}, status=422)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)

    return render(request, 'modules/login.html')

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        # messages.success(request, "Logged out Successfully")
    return redirect("login")

def users(request):
    users = CustomUser.objects.select_related('role').all()
    # print(users)
    context = {
        'page_title': "Users",
        'users': users,
    }    
    return render(request,"modules/masters/users.html",context)

def user_role(request):
    user_roles = UserRole.objects.all()
    context = {
        'page_title': "User Roles",
        'user_roles': user_roles,
    }    
    return render(request,"modules//masters/user_role.html",context)