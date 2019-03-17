from django.db import models


class Banner(models.Model):
    """
    首页幻灯片
    """
    title = models.CharField(max_length=32, verbose_name='标题')
    overview = models.CharField(max_length=128, verbose_name='概述')
    img_url = models.CharField(max_length=200, verbose_name='图片链接')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '首页幻灯片管理'
        verbose_name_plural = verbose_name
        ordering = ('-created',)

    def __str__(self):
        return self.title
