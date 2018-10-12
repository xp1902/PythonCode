from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles
from django.conf.urls import url
from . import views


app_name = 'tlion'

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^article/(?P<pk>[0-9]+)/$', views.article_page, name='article_page'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
    url(r'^tag/(?P<pk>[0-9]+)/$', views.tag, name='tag'),

    url(r'^edit/(?P<article_id>[0-9]+)/$', views.edit_page, name='edit_page'),
    url(r'^modify/action/$', views.modify_action, name='modify_action'),
    url(r'^edit/action/$', views.edit_action, name='edit_action'),
    url(r'^contact/', views.contact, name='contact'),

    url(r'^likes/(?P<article_id>[0-9]+)/$', views.collect_likes, name='likes'),
    url(r'^views/$', views.collect_views, name='views'),
]
urlpatterns += staticfiles_urlpatterns()
