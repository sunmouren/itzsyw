from django.contrib import admin

from .models import About, QRImage, OrderEmail


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['id', 'summary', 'created']


@admin.register(QRImage)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['id', 'img_url', 'is_active', 'created']


@admin.register(OrderEmail)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'created']
