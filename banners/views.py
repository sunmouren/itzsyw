from django.conf import settings
from django.http import JsonResponse
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Banner


class UploadBanner(LoginRequiredMixin, View):
    def post(self, request):
        if request.is_ajax():
            title = request.POST.get('title', None)
            overview = request.POST.get('overview', None)
            img_url = request.POST.get('srcUrl', None)
            if title and overview and img_url:
                try:
                    new_banner = Banner(title=title, overview=overview)
                    new_banner.img_url = settings.DOMAIN + img_url
                    new_banner.save()
                    return JsonResponse({'msg': 'ok'})
                except BaseException:
                    return JsonResponse({'msg': 'ko'})
        return JsonResponse({'msg': 'ko'})
