from django.contrib import admin

from apps.base.models import Application

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'number', 'message')
    list_filter = ('user', 'email')
    search_fields = ('user', 'email', 'number')
    list_per_page = 25

admin.site.register(Application, ApplicationAdmin)
