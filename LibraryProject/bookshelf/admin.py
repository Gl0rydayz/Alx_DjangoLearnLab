from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

# Import the CustomUser model
CustomUser = get_user_model()

# Define the CustomUserAdmin class if not already defined
class CustomUserAdmin(UserAdmin):
    pass  # Customize this class if needed

# Register the CustomUser model with the CustomUserAdmin class
admin.site.register(CustomUser, CustomUserAdmin)