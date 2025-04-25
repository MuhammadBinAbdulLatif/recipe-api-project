"""Django admin customization"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core import models
class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users"""
    ordering = ['id']
    list_display = ['email', 'name']

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Personal Info', {'fields': ('name',)}),
    )

    add_fieldsets = (  # <- fixed this line
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser'
            )
        }),
    )

admin.site.register(models.User, UserAdmin)