from django.contrib import admin
from .models import Job, Application


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'company_name',
        'location',
        'job_type',
        'salary',
        'is_active',
        'created_at',
    )
    list_filter = ('job_type', 'is_active', 'created_at')
    search_fields = ('title', 'company_name', 'location')
    ordering = ('-created_at',)

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'job',
        'candidate',
        'status',
        'applied_at',
    )
    list_filter = ('status', 'applied_at')
    search_fields = ('job__title', 'candidate__username')
    ordering = ('-applied_at',)

