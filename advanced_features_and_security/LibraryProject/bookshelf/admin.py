from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import Book, CustomUser

# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """
    Custom admin configuration for the CustomUser model.
    Extends Django's built-in UserAdmin with additional fields.
    """
    
    # Fields to display in the list view
    list_display = ('email', 'username', 'first_name', 'last_name', 'date_of_birth', 'is_staff', 'is_active')
    
    # Fields that can be used for searching
    search_fields = ('email', 'username', 'first_name', 'last_name')
    
    # Filters to display on the right sidebar
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'date_joined', 'date_of_birth')
    
    # Fieldsets for the detail/edit view
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'date_of_birth', 'profile_photo')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    
    # Fieldsets for adding a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'date_of_birth', 'profile_photo')}),
    )
    
    # Ordering
    ordering = ('email',)
    
    # Make email the primary field for user identification
    filter_horizontal = ('groups', 'user_permissions',)
    
    # Customize form help text
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if 'date_of_birth' in form.base_fields:
            form.base_fields['date_of_birth'].help_text = "Enter the user's date of birth (YYYY-MM-DD format)"
        if 'profile_photo' in form.base_fields:
            form.base_fields['profile_photo'].help_text = "Upload a profile photo for the user"
        return form


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for the Book model.
    Provides enhanced display, filtering, and search capabilities.
    """
    
    # Fields to display in the list view
    list_display = ('title', 'author', 'publication_year', 'added_by', 'id')
    
    # Fields that can be used for searching
    search_fields = ('title', 'author', 'added_by__username', 'added_by__email')
    
    # Filters to display on the right sidebar
    list_filter = ('publication_year', 'author', 'added_by')
    
    # Fields to display in the detail/edit view
    fields = ('title', 'author', 'publication_year', 'added_by')
    
    # Number of items to display per page
    list_per_page = 20
    
    # Enable ordering by clicking on column headers
    ordering = ('title',)
    
    # Make fields read-only (optional - can be removed if you want full editing)
    readonly_fields = ('id',)
    
    # Customize the admin list view title
    list_display_links = ('title', 'author')
    
    # Add date hierarchy if you had a date field (optional)
    # date_hierarchy = 'publication_year'
    
    # Customize the admin change form title
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['title'].help_text = "Enter the full title of the book (max 200 characters)"
        form.base_fields['author'].help_text = "Enter the author's name (max 100 characters)"
        form.base_fields['publication_year'].help_text = "Enter the year the book was published"
        return form
