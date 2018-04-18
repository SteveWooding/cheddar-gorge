"""Control how models are displayed on the Django admin site."""
from django.contrib import admin
from .models import Story, Word

class WordInline(admin.TabularInline):
    """Class to display words that belong to a story inline with that story."""
    model = Word
    extra = 1

class StoryAdmin(admin.ModelAdmin):
    """Defines attributes for displaying a story."""
    inlines = [WordInline]

admin.site.register(Story, StoryAdmin)
