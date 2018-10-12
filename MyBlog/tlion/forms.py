from django import forms

from .models import Article
from . import models


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        type = (
            ('p', 'publish'),
            ('d', 'draft')
        )
        author = models.User.objects.all().values_list('id', 'username')

        cate = models.Category.objects.all().values_list('id', 'name')

        tags = models.Tag.objects.all().values_list('id', 'name')

        fields = ['title', 'content', 'status', 'author', 'category', 'tags', 'head_img']

        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': "请输入标题",
            }),

            'content': forms.Textarea(attrs={
                'placeholder': '请输入内容...', }),

            'status': forms.Select(choices=type),

            'author': forms.Select(choices=author),

            'cagetory': forms.Select(choices=cate),

            'tag': forms.CheckboxSelectMultiple(choices=tags),
        }
