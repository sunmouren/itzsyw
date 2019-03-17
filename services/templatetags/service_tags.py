# encoding: utf-8
"""
@author: Sunmouren
@contact: sunxuechao1024@gmail.com
@time: 2019/3/15 20:36
@desc: 
"""

from django import template

from ..models import Service


register = template.Library()


@register.simple_tag
def get_hot_service_list(count=3):
    """
    获取热门服务
    :param count:
    :return:
    """
    return Service.objects.order_by('view_count')[:count]
