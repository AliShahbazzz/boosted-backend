from django.contrib import admin

# local import here.
from .models import *

@admin.register(ContactUs)
class FeedbackFormAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'message', 'created', 'updated']
    list_filter =  ['name', 'email']
    search_fields = ['name', 'email']

