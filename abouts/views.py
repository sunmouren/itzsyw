from django.shortcuts import render
from django.views.generic import View

from .models import About, QRImage


class AboutDetail(View):
    def get(self, request):
        current_page = 'abouts'
        abouts = About.objects.all()
        about = abouts[0] if abouts else None

        qr_images = QRImage.objects.all()
        return render(request, 'about-us.html', {
            'about': about,
            'qr_images': qr_images,
            'current_page': current_page,
        })

