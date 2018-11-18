from django.contrib import admin
from accounts.models import Activity_Log

@admin.register(Activity_Log)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ['date_time', 'username', 'activity',]
    list_filter = ['activity',]
