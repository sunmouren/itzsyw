# Generated by Django 2.1.7 on 2019-03-17 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abouts', '0002_auto_20190317_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='qrimage',
            name='title',
            field=models.CharField(max_length=64, null=True, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='about',
            name='purpose',
            field=models.CharField(max_length=200, null=True, verbose_name='服务宗旨'),
        ),
        migrations.AlterField(
            model_name='about',
            name='summary',
            field=models.TextField(null=True, verbose_name='摘要'),
        ),
        migrations.AlterField(
            model_name='qrimage',
            name='img_url',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='链接地址'),
        ),
        migrations.AlterField(
            model_name='qrimage',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='是否展示'),
        ),
    ]
