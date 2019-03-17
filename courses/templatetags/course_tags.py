# encoding: utf-8
"""
@author: Sunmouren
@contact: sunxuechao1024@gmail.com
@time: 2019/3/3 16:35
@desc: 
"""

from django import template

from ..models import Course, Video


register = template.Library()


@register.simple_tag
def get_hot_course(count=5):
    """
    获取热门课程
    :param count:
    :return:
    """
    return Course.objects.order_by('view_count')[:count]


@register.simple_tag
def get_hot_video(count=5):
    """
    获取热门课程
    :param count:
    :return:
    """
    return Video.objects.order_by('view_count')[:count]

