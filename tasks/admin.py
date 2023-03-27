from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("creacion",)

# Register your models here.
admin.site.register(Task, TaskAdmin)