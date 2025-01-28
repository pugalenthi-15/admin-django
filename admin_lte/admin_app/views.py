from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from django.core.paginator import Paginator



# def main(request):
#     return render(request,"layouts/main.html")
def dashboard(request):
    return render(request, "modules/dashboard.html")


# def login(request):
#     return render(request,"modules/login.html")


@csrf_exempt
def login_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    else:
        if request.method == "POST":
            try:
                data = json.loads(request.body)  # Parse the AJAX JSON body
                email = data.get("email")
                password = data.get("password")

                user = CustomUser.objects.get(email=email)
                if user and user.password == password:
                    login(request, user)
                    return JsonResponse({"success": True}, status=200)
                else:
                    return JsonResponse(
                        {"success": False, "error": "Invalid email or password"}, status=422
                    )

            except CustomUser.DoesNotExist:
                return JsonResponse(
                    {"success": False, "error": "Invalid email or password"}, status=422
                )
            except Exception as e:
                return JsonResponse({"success": False, "error": str(e)}, status=500)

        return render(request, "modules/login.html")


def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        # messages.success(request, "Logged out Successfully")
    return redirect("login")


def users(request):
    page_obj = paginate_model(
        request, CustomUser, per_page=10, select_related_fields=["role"]
    )
    for user in page_obj.object_list:
        print(f'User: {user.name}, Role: {user.role.name if user.role else "No Role"}')
    context = {
        "page_title": "User Roles",
        "data": page_obj.object_list,  # List of user roles for the current page
        "page_obj": page_obj,  # The Page object to render pagination controls
    }
    return render(request, "modules/masters/users.html", context)

def state(request):
    page_obj = paginate_model(request, State)
    context = {
        "page_title": "States",
        "data": page_obj.object_list,  # List of user roles for the current page
        "page_obj": page_obj,  # The Page object to render pagination controls
    }
    return render(request, "modules/masters/state.html", context)


def user_role(request):
    page_obj = paginate_model(request, UserRole)

    context = {
        "page_title": "User Roles",
        "data": page_obj.object_list,  # List of user roles for the current page
        "page_obj": page_obj,  # The Page object to render pagination controls
    }
    return render(request, "modules/masters/user_role.html", context)


def paginate_model(request, model_class, per_page=10, select_related_fields=None):
    # Optionally include related foreign key data using select_related
    objects = model_class.objects.all().order_by("-id")

    if select_related_fields:
        objects = objects.select_related(*select_related_fields)
    # print(objects.query)
    # Set up pagination
    paginator = Paginator(objects, per_page)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return page_obj
