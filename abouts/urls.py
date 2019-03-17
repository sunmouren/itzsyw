# encoding: utf-8
"""
@author: Sunmouren
@contact: sunxuechao1024@gmail.com
@time: 2019/3/17 17:08
@desc: 
"""

from django.urls import path

from .views import AboutDetail

app_name = 'abouts'


urlpatterns = [
   path('us/', AboutDetail.as_view(), name='about-us'),
]