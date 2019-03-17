# encoding: utf-8
"""
@author: Sunmouren
@contact: sunxuechao1024@gmail.com
@time: 2019/3/15 20:18
@desc: 
"""

from django import template

from ..models import Banner


register = template.Library()


@register.simple_tag
def get_banners_list():
    """
    获取幻灯片列表
    :return:
    """
    return Banner.objects.all()
