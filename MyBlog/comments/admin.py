from django.contrib import admin
from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'pub_time', 'email', 'url', 'article']

admin.site.register(Comment, CommentAdmin)