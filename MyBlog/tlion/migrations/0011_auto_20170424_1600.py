# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-24 08:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tlion', '0010_article_comments_num'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.AlterField(
            model_name='article',
            name='head_img',
            field=models.ImageField(upload_to='uploads'),
        ),
        migrations.DeleteModel(
            name='UserGroup',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
