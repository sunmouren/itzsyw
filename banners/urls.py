# encoding: utf-8
"""
@author: Sunmouren
@contact: sunxuechao1024@gmail.com
@time: 2019/3/17 0:09
@desc: 
"""
from django.urls import path

from .views import UploadBanner

app_name = 'banners'


urlpatterns = [
   path('upload/', UploadBanner.as_view()),
]