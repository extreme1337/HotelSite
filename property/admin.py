from django.contrib import admin
from .models import Property, Category, Reserve

# Register your models here.
admin.site.register(Property)
admin.site.register(Category)
admin.site.register(Reserve)
