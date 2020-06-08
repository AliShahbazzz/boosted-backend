from django.contrib import admin

# local import here.
from .models import *


@admin.register(UserResume)
class FeedbackFormAdmin(admin.ModelAdmin):
    list_display = ['user', 'resume_number', 'created']
    list_filter = ['user', 'position', 'created']
    #prepopulated_fields = {'slug':('title',)}
    search_fields = ['name']
