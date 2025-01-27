from django.contrib import admin
from .models import *

class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'created_by', 'created_at')
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile', 'role')

admin.site.register(UserRole, UserRoleAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
