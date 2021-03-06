# Generated by Django 2.1.7 on 2019-03-15 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='标题')),
                ('overview', models.CharField(max_length=128, verbose_name='概述')),
                ('img_url', models.CharField(max_length=200, verbose_name='图片链接')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '首页幻灯片管理',
                'verbose_name_plural': '首页幻灯片管理',
                'ordering': ('-created',),
            },
        ),
    ]
