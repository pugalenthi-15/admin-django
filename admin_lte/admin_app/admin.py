from django.contrib import admin
from .models import *

class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'created_by', 'created_at')

admin.site.register(UserRole, UserRoleAdmin)
