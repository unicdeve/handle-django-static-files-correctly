from django.contrib import admin
from .models import Product
from django.utils.html import format_html

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_preview', 'formatted_price', 'category', 'is_available', 'created_at')
    list_filter = ('category', 'is_available', 'created_at')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at', 'updated_at')
    list_editable = ('is_available',)
    
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'price', 'category')
        }),
        ('Media', {
            'fields': ('image',),
            'classes': ('collapse',)
        }),
        ('Status', {
            'fields': ('is_available',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            print(obj.image)
            return format_html(f'<img src="{obj.image.url}" style="max-width: 50px; max-height: 50px;" />')
        return None
    
    image_preview.allow_tags = True
    image_preview.short_description = 'Image'
