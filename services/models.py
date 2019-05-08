from django.db import models
from django.urls import reverse


class Service(models.Model):
    """
    服务类型表
    """
    title = models.CharField(max_length=20, verbose_name='服务名称')
    overview = models.TextField(verbose_name='描述', blank=True, null=True)
    price = models.CharField(max_length=10, verbose_name='价格(元)')
    img_url = models.CharField(max_length=200, verbose_name='图片链接', blank=True, null=True)
    view_count = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True, verbose_name='是否激活')

    def get_absolute_url(self):
        return reverse('services:service-detail', args=[self.id])

    def add_view_count(self):
        self.view_count += 1
        self.save()

    def get_order_count(self):
        return self.orders.count()

    class Meta:
        verbose_name = '服务类型'
        verbose_name_plural = verbose_name
        ordering = ('title',)

    def __str__(self):
        return self.title


class Order(models.Model):
    """
    订单表
    """
    CONTACT_WAY_CHOICES = (
        ('qq', 'QQ号'),
        ('tel', '手机号码')
    )
    service = models.ForeignKey('Service', on_delete=models.CASCADE,
                                related_name='orders', verbose_name='服务类型')
    name = models.CharField(max_length=8, verbose_name='姓名')
    contact_way = models.CharField(max_length=8, choices=CONTACT_WAY_CHOICES,
                                   default=CONTACT_WAY_CHOICES[0], verbose_name='联系方式')
    contact_info = models.CharField(max_length=20, verbose_name='联系信息')
    is_finish = models.BooleanField(default=False, verbose_name='是否完成')
    created = models.DateTimeField(auto_now_add=True, verbose_name='下单时间')

    class Meta:
        verbose_name = '服务订单'
        verbose_name_plural = verbose_name
        ordering = ('-created',)

    def __str__(self):
        return self.service.title
