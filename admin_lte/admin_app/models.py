from django.db import models
from django.contrib.auth.models import User


class UserRole(models.Model):
    name = models.CharField(max_length=255, unique=True)  # Role name
    status = models.BooleanField(default=1)  # Active status
    created_at = models.DateTimeField(
        auto_now_add=True
    )  # Timestamp when the role was created
    updated_at = models.DateTimeField(
        auto_now=True
    )  # Timestamp when the role was last updated
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="userrole_created_by"
    )  # Reference to the user who created the role
    updated_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="userrole_updated_by"
    )  # Reference to the user who last updated the role

    def __str__(self):
        return self.name
