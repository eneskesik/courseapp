from django.contrib import admin
from .models import Course, Category

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'slug', 'isActive']
    list_display_links = ['title', 'slug']
    readonly_fields = ['slug']
    list_filter = ['date', 'isActive']
    list_editable = ['isActive']
    search_fields = ['title', 'description']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    list_display_links = ['name', 'slug']
    search_fields = ['name']