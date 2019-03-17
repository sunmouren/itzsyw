"""zw_online URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.http import JsonResponse
from django.urls import path, include
from django.views.generic import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin

from qiniu import Auth


class GetQiNiuToken(LoginRequiredMixin, View):
    """
    获取七牛云的上传文件token
    """

    def get(self, request):
        try:
            q = Auth(settings.ACCESS_KEY, settings.SECRET_KEY)
            token = q.upload_token(bucket=settings.BUCKET_NAME, key=None, expires=3600)

            return JsonResponse({'msg': 'ok', 'token': token, 'username': request.user.username})
        except BaseException:
            return JsonResponse({'msg': 'ko'})


urlpatterns = [
    path('admin/', admin.site.urls),
    # index
    path('', TemplateView.as_view(template_name='index.html', extra_context={'current_page': 'index'}), name='index'),
    # service
    path('service/', include('services.urls', namespace='services')),
    # course
    path('course/', include('courses.urls', namespace='courses')),
    # banner
    path('banner/', include('banners.urls', namespace='banners')),
    # abouts
    path('about/', include('abouts.urls', namespace='abouts')),
    # upload token
    path('upload/token/', GetQiNiuToken.as_view()),

]







