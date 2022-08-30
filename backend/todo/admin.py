from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')
    #list_filter = ('completed',)
    #search_fields = ('title', 'description')
    #ordering = ('completed',)
    #fields = ('title', 'description', 'completed')
    #readonly_fields = ('completed',)
    #actions = ['make_completed']

    #def make_completed(self, request, queryset):
    #    queryset.update(completed=True)
    #make_completed.short_description = 'Mark selected as completed'

#Register your models here.

admin.site.register(Todo, TodoAdmin)
