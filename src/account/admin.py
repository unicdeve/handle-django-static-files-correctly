from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.utils.html import format_html

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'avatar_preview', 'username', 'email', 'first_name', 'last_name', 'is_active',)
    list_filter = ('is_staff', 'is_active', 'created_at')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('-created_at',)
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('avatar', 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    readonly_fields = ('created_at', 'updated_at')
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('avatar', 'email', 'password1', 'password2', 'first_name', 'last_name'),
        }),
    )

    def avatar_preview(self, obj):
        if obj.avatar:
            print(obj.avatar)
            return format_html(f'<img src="{obj.avatar.url}" style="max-width: 50px; max-height: 50px;" />')
        return None
    
    avatar_preview.allow_tags = True
    avatar_preview.short_description = 'Avatar'
