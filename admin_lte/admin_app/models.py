from django.db import models
import uuid
from django.contrib.auth.models import User,AbstractBaseUser

class UserRole(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, null=True)  # UUID field
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

class CustomUser(AbstractBaseUser):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, null=True)  # UUID field
    name = models.CharField(max_length=255)  # User name
    mobile = models.CharField(max_length=15)  # Mobile number
    email = models.EmailField(unique=True)  # Email address
    password = models.CharField(max_length=255)  # Password
    role = models.ForeignKey(
        UserRole, on_delete=models.SET_NULL, null=True, related_name="customuser_role"
    )  # Reference to the role
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="customuser_created_by"
    )  # Reference to the user who created this record
    updated_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="customuser_updated_by"
    )  # Reference to the user who last updated this record
    status = models.BooleanField(default=1)  # Active status
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the record was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when the record was last updated
    last_login = models.DateTimeField(auto_now=True, null=True, blank=True)  # Automatically updated field

    USERNAME_FIELD = 'email'  # Define the unique field for authentication
    REQUIRED_FIELDS = ['name']  # Define the fields that are required for creating a user

    def __str__(self):
        return self.name
    
#state table
class State(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, null=True)  # UUID field
    name = models.CharField(max_length=255, unique=True)  # Role name
    status = models.BooleanField(default=1)  # Active status
    created_at = models.DateTimeField(
        auto_now_add=True
    )  # Timestamp when the role was created
    updated_at = models.DateTimeField(
        auto_now=True
    )  # Timestamp when the role was last updated
    created_by = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, null=True, related_name="state_created_by"
    )  # Reference to the user who created the role
    updated_by = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, null=True, related_name="state_updated_by"
    )  # Reference to the user who last updated the role

    def __str__(self):
        return self.name