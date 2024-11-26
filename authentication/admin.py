# admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Specify the fields to display in the list view and form view
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_active']
    list_filter = ['is_active', 'is_staff']
    search_fields = ['email', 'username']
    ordering = ['username']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('middle_name', 'suffix', 'contact_number', 'dob', 'gender', 'address', 'student_type', 'course', 'year_level', 'student_id')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('middle_name', 'suffix', 'contact_number', 'dob', 'gender', 'address', 'student_type', 'course', 'year_level', 'student_id')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
