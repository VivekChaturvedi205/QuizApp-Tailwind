from django.contrib import admin
from .models import students

@admin.register(students)
class studentsAdmin(admin.ModelAdmin):
    list_display=['name', 'city','age','createdAt','updatedAt']
