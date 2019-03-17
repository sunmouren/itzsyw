from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin

from abouts.models import OrderEmail

from .models import Service, Order


class ServiceList(View):
    """
    服务列表
    """
    def get(self, request):
        current_page = 'services'
        services = Service.objects.all()
        return render(request, 'service-list.html', {
            'services': services,
            'current_page': current_page
        })

    def post(self, request):
        if request.is_ajax():
            sid = request.POST.get('sid', None)
            name = request.POST.get('name', None)
            way = request.POST.get('way', None)
            info = request.POST.get('info', None)
            if sid and way and info:
                try:
                    service = Service.objects.get(id=int(sid))
                    new_order = Order(service=service, name=name, contact_way=way, contact_info=info)
                    new_order.save()
                    send_mail_to_admin(new_order)
                    return JsonResponse({'msg': 'ok'})
                except Service.DoesNotExist:
                    return JsonResponse({'msg': 'ko'})
        return JsonResponse({'msg': 'ko'})


class ServiceDetail(View):
    """
    服务详情
    """
    def get(self, request, sid):
        service = get_object_or_404(Service, id=int(sid))
        return render(request, 'service-detail.html', {'service': service})


def send_mail_to_admin(order=None):
    """
    如果有信订单，就通知管理员
    :param order:
    :return:
    """
    if order:
        subject = "IT掌上运维，又有新订单了，请尽快处理!"
        message = "服务类型: {0}, 姓名: {1}, 联系方式: {2}, 联系信息: {3}, 下单时间: {4}".format(
            order.service.title,
            order.name,
            order.contact_way,
            order.contact_info,
            order.created
        )

        try:
            recipient_list = [email.email for email in OrderEmail.objects.all()]
            send_status = send_mail(subject, message, settings.EMAIL_FROM, recipient_list)
            if send_status:
                pass
        except BaseException:
            pass


class UploadService(LoginRequiredMixin, View):
    def post(self, request):
        if request.is_ajax():
            title = request.POST.get('title', None)
            overview = request.POST.get('overview', None)
            price = request.POST.get('price', None)
            img_url = request.POST.get('srcUrl', None)
            if title and overview and price and img_url:
                try:
                    new_service = Service(title=title, overview=overview, price=price)
                    new_service.img_url = settings.DOMAIN + img_url
                    new_service.save()
                    return JsonResponse({'msg': 'ok'})
                except BaseException:
                    return JsonResponse({'msg': 'ko'})
        return JsonResponse({'msg': 'ko'})



