from django.conf.urls import url

from . import views

app_name = 'comments'
urlpatterns = [
    url(r'^article/(?P<article_id>[0-9]+)/$', views.article_comment, name='article_comment'),

]
