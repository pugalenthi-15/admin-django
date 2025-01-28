from django.contrib import admin
from .models import *

class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'created_by', 'created_at')
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile', 'role')
class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'created_by')

admin.site.register(UserRole, UserRoleAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(State, StateAdmin)
