"""定义learning_logs的URL模式"""
from django.conf.urls import url
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),

    url(r'^topics/$', views.topics, name='topics'),
]
