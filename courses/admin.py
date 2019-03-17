from django.contrib import admin

from .models import Course, Video


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """
    课程管理
    """
    list_display = ['id', 'title', 'created']


@admin.register(Video)
class Video(admin.ModelAdmin):
    """
    视频管理
    """
    list_display = ['id', 'course', 'title', 'url', 'created']
    list_filter = ['course', 'created']
