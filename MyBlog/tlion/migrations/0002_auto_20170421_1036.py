# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-21 02:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tlion', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-modifies_time']},
        ),
        migrations.AddField(
            model_name='article',
            name='likes',
            field=models.PositiveIntegerField(default=0, verbose_name='点赞数'),
        ),
        migrations.AddField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('p', 'Published'), ('d', 'Drafted')], default='p', max_length=1, verbose_name='文章状态'),
        ),
        migrations.AddField(
            model_name='article',
            name='views',
            field=models.PositiveIntegerField(default=0, verbose_name='浏览量'),
        ),
        migrations.AddField(
            model_name='category',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='创建时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='modifies_time',
            field=models.DateTimeField(auto_now=True, verbose_name='修改时间'),
        ),
        migrations.AlterField(
            model_name='article',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='excerpt',
            field=models.CharField(blank=True, max_length=54, null=True),
        ),
    ]