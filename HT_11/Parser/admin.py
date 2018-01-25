from django.contrib import admin
from .models import *


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'goal']


@admin.register(Askstories)
class AskstoriesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'time', 'descendants',
                    'by', 'kids', 'type', 'score', 'url']
