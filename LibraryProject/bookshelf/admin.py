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

# Permissions and Groups Setup

## Custom Permissions
# The `Book` model includes the following custom permissions:
# - `can_view`: Allows viewing books.
# - `can_create`: Allows creating books.
# - `can_edit`: Allows editing books.
# - `can_delete`: Allows deleting books.

## Groups
# The following groups are set up with specific permissions:
# - **Viewers**: `can_view`
# - **Editors**: `can_view`, `can_create`, `can_edit`
# - **Admins**: `can_view`, `can_create`, `can_edit`, `can_delete`

## Views
# Permissions are enforced in the following views:
# - `book_list`: Requires `can_view`
# - `book_create`: Requires `can_create`
# - `book_edit`: Requires `can_edit`
# - `book_delete`: Requires `can_delete`

## Testing
# 1. Create test users and assign them to groups.
# 2. Log in as these users and verify access to views.