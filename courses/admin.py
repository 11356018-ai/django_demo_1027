from django.contrib import admin

from .models import Course, Enrollment


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'credits', 'instructor', 'schedule', 'location', 'capacity', 'enrolled_count', 'status', 'proposer', 'created_at')
    list_filter = ('status', 'credits')
    search_fields = ('code', 'name', 'instructor', 'proposer__username')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('課程基本資訊', {
            'fields': ('code', 'name', 'credits', 'description')
        }),
        ('上課資訊', {
            'fields': ('instructor', 'schedule', 'location', 'capacity')
        }),
        ('審核資訊', {
            'fields': ('status', 'proposer')
        }),
        ('時間資訊', {
            'fields': ('created_at', 'updated_at')
        }),
    )
    actions = ['approve_courses', 'reject_courses']

    def approve_courses(self, request, queryset):
        queryset.update(status=Course.STATUS_APPROVED)

    approve_courses.short_description = '核准選取的課程'

    def reject_courses(self, request, queryset):
        queryset.update(status=Course.STATUS_REJECTED)

    reject_courses.short_description = '退回選取的課程'


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'enrolled_at')
    search_fields = ('student__username', 'course__code', 'course__name')
    readonly_fields = ('enrolled_at',)
    list_filter = ('course',)
