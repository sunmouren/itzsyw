from django.contrib import admin

from .models import Service, Order


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """
    服务类型管理
    """
    list_display = ['id', 'title', 'price', 'is_active']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    订单管理
    """
    list_display = ['id', 'service', 'name', 'contact_way',
                    'contact_info', 'created', 'is_finish']
    list_filter = ['created', 'is_finish']
