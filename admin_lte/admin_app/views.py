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
                        {"success": False, "error": "Invalid email or password"},
                        status=422,
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
    return render(request, "modules/masters/users/users.html", context)

def user_role(request):
    page_obj = paginate_model(request, UserRole)

    context = {
        "page_title": "User Roles",
        "data": page_obj.object_list,  # List of user roles for the current page
        "page_obj": page_obj,  # The Page object to render pagination controls
    }
    return render(request, "modules/masters/users/user_role.html", context)

def state(request):
    page_obj = paginate_model(request, State)
    context = {
        "page_title": "States",
        "data": page_obj.object_list,  # List of user roles for the current page
        "page_obj": page_obj,  # The Page object to render pagination controls
    }
    return render(request, "modules/masters/state/index.html", context)

def state_create(request):
    context = {
        "module_name": "State",
        "module_function": "Add",
        "method": "POST",
        "route": "store",
    }
    # print(context)
    return render(request, "modules/masters/state/add_edit.html", context)

def add_state(request):
    if (
        request.method != "POST"
        or request.headers.get("X-Requested-With") != "XMLHttpRequest"
    ):
        return JsonResponse(
            {"status": "error", "message": "Invalid request"}, status=400
        )

    try:
        data = json.loads(request.body)
        name = data.get("name", "").strip()
        status = int(data.get("status", 1))

        if not name:
            return JsonResponse(
                {"status": "error", "message": "State name is required"}, status=422
            )

        State.objects.create(name=name, status=status)

        return JsonResponse(
            {"status": "success", "message": "State added successfully!"}, status=200
        )

    except Exception as e:
        return JsonResponse(
            {"status": "error", "message": f"An error occurred: {str(e)}"}, status=500
        )

def state_edit(request, state_id):
    try:
        state = State.objects.get(id=state_id)
        context = {
            "module_name": "State",
            "module_function": "Edit",
            "method": "PUT",
            "route": f"update/{state.id}",
            "data": state,
        }
        # print(context)
        return render(request, "modules/masters/state/add_edit.html", context)
    except State.DoesNotExist:
        return redirect("state_list")  # Redirect to the state list page if not found

def state_update(request, state_id):
    if (request.method != "PUT"
        or request.headers.get("X-Requested-With") != "XMLHttpRequest"):
        return JsonResponse(
            {"status": "error", "message": "Invalid request"}, status=400
        )

    try:
        data = json.loads(request.body)
        name = data.get("name", "").strip()
        status = int(data.get("status", 0))

        if not name:
            return JsonResponse(
                {"status": "error", "message": "State name is required"}, status=422
            )

        state = State.objects.get(id=state_id)
        state.name = name
        state.status = status
        state.save()

        return JsonResponse(
            {"status": "success", "message": "State updated successfully!"}, status=200
        )

    except State.DoesNotExist:
        return JsonResponse(
            {"status": "error", "message": "State not found"}, status=404
        )
    except Exception as e:
        return JsonResponse(
            {"status": "error", "message": f"An error occurred: {str(e)}"}, status=500
        )

def state_delete(request, state_id):
    if request.method == 'DELETE':
        try:
            item = State.objects.get(id=state_id)
            item.delete()
            return JsonResponse({'message': 'Item deleted successfully'}, status=200)
        except State.DoesNotExist:
            return JsonResponse({'error': 'Item not found'}, status=404)
    return JsonResponse({'error': 'Invalid request'}, status=400)


# Helper Functions
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


