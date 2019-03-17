from django.db import models


class About(models.Model):

    team_name = models.CharField(max_length=64, null=True, verbose_name='团队名称')
    summary = models.TextField(null=True, verbose_name='摘要')
    purpose = models.CharField(null=True, max_length=200, verbose_name='服务宗旨')
    service = models.TextField(null=True, verbose_name='特色服务')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '团队介绍管理'
        verbose_name_plural = verbose_name
        ordering = ('-created',)

    def __str__(self):
        return self.summary[0]


class QRImage(models.Model):
    title = models.CharField(max_length=64, verbose_name='标题', null=True)
    img_url = models.CharField(max_length=200, blank=True, null=True, verbose_name='链接地址')

    is_active = models.BooleanField(default=True, verbose_name='是否展示')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '二维码图片管理'
        verbose_name_plural = verbose_name
        ordering = ('-created',)

    def __str__(self):
        return self.title


class OrderEmail(models.Model):
    """
    接收订单邮箱
    """
    email = models.EmailField()
    is_active = models.BooleanField(default=True, verbose_name='是否接收')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '接收订单邮箱管理'
        verbose_name_plural = verbose_name
        ordering = ('-created',)

    def __str__(self):
        return self.email

