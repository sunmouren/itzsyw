from django.db import models
from django.urls import reverse


class Course(models.Model):
    """
    课程数据库表
    """
    title = models.CharField(max_length=32, verbose_name='课程名')
    overview = models.TextField(blank=True, null=True, verbose_name='概述')
    view_count = models.PositiveIntegerField(default=0, verbose_name='浏览量')
    img_url = models.CharField(max_length=200, verbose_name='图片链接', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '课程管理'
        verbose_name_plural = verbose_name
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('courses:course-detail', args=[self.pk])

    def add_view_count(self):
        self.view_count += 1
        self.save()

    def get_video_count(self):
        return self.video_set.count()

    def __str__(self):
        return self.title


class Video(models.Model):
    """
    视频数据库表
    """
    course = models.ForeignKey('Course', on_delete=models.CASCADE, verbose_name='所属课程')
    title = models.CharField(max_length=64, verbose_name='标题')
    overview = models.TextField(blank=True, null=True, verbose_name='概述')
    url = models.CharField(max_length=250, verbose_name='视频url')
    view_count = models.PositiveIntegerField(default=0, verbose_name='播放量')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '视频管理'
        verbose_name_plural = verbose_name
        ordering = ('created', )

    def get_absolute_url(self):
        return reverse('courses:video-detail', args=[self.pk])

    def __str__(self):
        return self.title
