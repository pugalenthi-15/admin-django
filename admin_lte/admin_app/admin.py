from django.contrib import admin
from .models import *

class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'status','created_at')
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["email", "get_full_name", "mobile", "role"]
    
    def get_full_name(self, obj):
        return obj.get_full_name()

    get_full_name.short_description = "Name"  # Column label in admin panel

class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')

admin.site.register(UserRole, UserRoleAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(State, StateAdmin)
