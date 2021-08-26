from django.contrib import admin
from .models import Task


#admin.site.register(Task)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'complete', 'created', 'updated']
    # prepopulated_fields = {'slug': ('name',)}
# Register your models here.
