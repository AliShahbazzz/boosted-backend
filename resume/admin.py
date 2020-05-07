from django.contrib import admin

# local import here.
from .models import *

class ContentInLine(admin.TabularInline):
    model = Content
    extra = 1

@admin.register(UserResume)
class FeedbackFormAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'position']
    list_filter =  ['name', 'position']
    # prepopulated_fields = {'slug':('title',)}
    search_fields = ['name']
    # list_editable = ['feedback_format']
    inlines = [
        ContentInLine,
    ]

admin.site.register(ContactDetail)
admin.site.register(Achievement)
admin.site.register(Skill)
admin.site.register(Interest)
admin.site.register(Internship)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Project)
admin.site.register(Certification)
admin.site.register(Recommendation)