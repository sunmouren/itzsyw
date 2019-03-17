# encoding: utf-8
"""
@author: Sunmouren
@contact: sunxuechao1024@gmail.com
@time: 2019/2/16 20:36
@desc: 
"""
from django.urls import path

from .views import CourseList, CourseDetail, VideoDetail, course_search, UploadCourse, UploadVideo

app_name = 'courses'


urlpatterns = [
    path('list/', CourseList.as_view(), name='course-list'),
    path('detail/<int:cid>/', CourseDetail.as_view(), name='course-detail'),
    path('video/<int:vid>/', VideoDetail.as_view(), name='video-detail'),
    path('search/', course_search, name='course-search'),
    path('upload/', UploadCourse.as_view()),
    path('video/upload/', UploadVideo.as_view()),
]