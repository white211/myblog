from django.conf.urls import url
from django.urls import path,re_path
from . import views
urlpatterns = [
    url(r'^index/',views.index),
    # re_path('article/(?P<article_id>[0-9]+)', views.page_article, name='article_id'),
    url(r'^article/(?P<article_id>[0-9]+)$', views.article_page, name='article_page'),
    url(r'^edit/$',views.edit_page,name='edit_page'),
    url(r'^edit_action/$',views.edit_action,name='edit_action'),
]

