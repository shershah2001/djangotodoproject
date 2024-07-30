from django.contrib import admin
from .models import TodoModel

@admin.register(TodoModel)
class TodoAdmin(admin.ModelAdmin):
    list_display=("id","name","roll_num","father_name","mother_name","phone","email","address","gender","father_image","mother_image","student_image")


