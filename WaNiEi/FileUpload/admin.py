from django.contrib import admin
from .models import File

# Register your models here.

admin.site.register(File)

class File(admin.ModelAdmin):
    list_display = ("file", "created_at")
    list_filter = ("created_at",)
