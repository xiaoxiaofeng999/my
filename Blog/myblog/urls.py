from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r"^home/",my_home,name="home"),# 首页
    url(r"^detail/(?P<id>\d+)$",detail,name='detail'),#展示页
    url(r"^search",search,name="search"),
    url(r"suibi$",my_suibi,name="suibi"),
    url(r"study",my_study,name="study"),

    url(r"^liuyian$",my_liuyian,name='liuyian'),
    url(r"^mine$",mine,name='mine')
]