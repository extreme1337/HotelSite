from django.contrib import admin
from .models import Property, Category, Reserve

class PropertyAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'category']
    search_fields = ['name', 'type']
    list_filter = ['category', 'type']

# Register your models here.
admin.site.register(Property, PropertyAdmin)
admin.site.register(Category)
admin.site.register(Reserve)
