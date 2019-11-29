"""定义learning_logs的URL模式"""
from django.urls import path
# from django.urls import path, include
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # 主页
    # url(r'^$', views.index, name='index'),
    #
    # url(r'^topics/$', views.topics, name='topics'),
    # url(r'^new_topic/$', views.new_topic, name='new_topic'),

    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    # path('new_topic/', views.new_topic, name='new_topic'),
]
