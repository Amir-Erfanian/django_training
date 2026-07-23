from django.contrib import admin
from .models import Student, Teacher, Course

admin.site.site_header = "School Administration"
admin.site.site_title = "School Admin"
admin.site.index_title = "Welcome to the School Dashboard"

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "age",
        "email",
    )

    search_fields = (
        "name",
        "email",
    )

    ordering = (
        "name",
    )

    list_filter = (
        "age",
    )
admin.site.register(Teacher)
admin.site.register(Course)