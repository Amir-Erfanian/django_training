from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "age", "email")
    search_fields = ("name", "email")
    list_filter = ("age",)
    list_editable = ("age",)
    readonly_fields = ("email",)