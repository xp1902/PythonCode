from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    modifies_time = models.DateTimeField('修改时间', auto_now=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):
    STATUS_CHOICES = (
        ('p', 'Published'),
        ('d', 'Drafted')
    )
    title = models.CharField(max_length=70, null=False)
    content = models.TextField()
    head_img = models.ImageField(upload_to='uploads/', blank=True, default='static/img/1.jpg')

    create_time = models.DateTimeField(auto_now_add=True)
    modifies_time = models.DateTimeField(auto_now=True)
    status = models.CharField('文章状态', max_length=1, choices=STATUS_CHOICES, default='p')
    excerpt = models.CharField(max_length=54, blank=True, null=True)

    views = models.PositiveIntegerField('浏览量', default=0)
    likes = models.PositiveIntegerField('点赞数', default=0)
    comments_num = models.PositiveIntegerField(default=0)

    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User)

    class Meta:
        # Meta 包含一系列选项，这里的 ordering 表示排序，- 号表示逆序。即当从数据库中取出文章时，其是按文章最后一次修改时间逆序排列的。
        ordering = ['-modifies_time']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tlion:article_page', kwargs={'pk': self.pk})


