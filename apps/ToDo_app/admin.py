from django.contrib import admin

from apps.ToDo_app.models import TodoListModel

# class Todo_Admin(admin.ModelAdmin):
#     list_display=['task','describe','is_completed','created_to']

# admin.site.register(Todo_Admin,TodoListModel)

admin.site.register(TodoListModel)
