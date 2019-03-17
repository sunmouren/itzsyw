# encoding: utf-8
"""
@author: Sunmouren
@contact: sunxuechao1024@gmail.com
@time: 2019/2/16 15:26
@desc: 
"""

from django.urls import path

from .views import ServiceList, ServiceDetail, UploadService

app_name = 'services'


urlpatterns = [
    path('list/', ServiceList.as_view(), name='service-list'),
    path('detail/<int:sid>/', ServiceDetail.as_view(), name='service-detail'),
    path('upload/', UploadService.as_view()),
]