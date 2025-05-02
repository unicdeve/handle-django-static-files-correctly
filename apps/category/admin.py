from django.contrib import admin
from .models import Category
from django.utils.html import format_html


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_preview', 'created_at', 'updated_at')
    list_filter = ('created_at',)
    search_fields = ('name',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('name', 'image')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" style="max-width: 50px; max-height: 50px;" />')
        return None
    
    image_preview.allow_tags = True
    image_preview.short_description = 'Image'
