from django.contrib import admin

# local import here.
from .models import *


@admin.register(UserResume)
class FeedbackFormAdmin(admin.ModelAdmin):
    list_display = ['user', 'resume_number', 'created', 'updated']
    list_filter = ['name', 'position']
    #prepopulated_fields = {'slug':('title',)}
    search_fields = ['name']
