from django.contrib import admin
from .models import Book

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for the Book model.
    Provides enhanced display, filtering, and search capabilities.
    """
    
    # Fields to display in the list view
    list_display = ('title', 'author', 'publication_year', 'id')
    
    # Fields that can be used for searching
    search_fields = ('title', 'author')
    
    # Filters to display on the right sidebar
    list_filter = ('publication_year', 'author')
    
    # Fields to display in the detail/edit view
    fields = ('title', 'author', 'publication_year')
    
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
