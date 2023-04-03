from django.contrib import admin
from todo.models import task
# Register your models here.

@admin.register(task)
class taskAdmin(admin.ModelAdmin):
    list_display = ['id','title','completed']