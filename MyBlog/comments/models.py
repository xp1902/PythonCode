from django.db import models
from django.utils.six import python_2_unicode_compatible


@python_2_unicode_compatible
class Comment(models.Model):
    pub_time = models.DateTimeField('评论发表时间', auto_now=True)
    content = models.TextField('评论内容', null=False)
    name = models.CharField('评论者名字', max_length=10, null=False)
    email = models.EmailField('评论者邮箱', max_length=255, null=False)
    url = models.URLField('评论者网址', max_length=255, blank=True, null=True)

    article = models.ForeignKey('tlion.Article', verbose_name='评论所属文章', on_delete=models.CASCADE, null=True)

    # 多级评论,是不是评论评论的当前的表(自己表),所以就得和自己做一个关联!
    # 这里在关联自己的时候必须设置一个related_name否则会报错冲突
    # 这里parent_comment,必须设置为可以为空,因为如果他是第一评论他是没有父ID的
    parent_comment = models.ForeignKey('self', related_name='p_comment', verbose_name='评论回复', default=None, blank=True, null=True)

    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.content[:20]


