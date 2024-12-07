from django.contrib import admin
from django.utils.html import format_html
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'is_active', 'display_image', 'link')  # Columns to display

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.image.url)
        return "No Image"
    
    display_image.short_description = 'Image'  # Column name in admin

admin.site.register(Project, ProjectAdmin)