from django.contrib import admin
from . import models

@admin.register(models.Todo)
class ToDoAdmin(admin.ModelAdmin):
    pass