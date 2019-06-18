
from django.conf.urls import url, include
from django.contrib import admin

# from .views import *
from myapp.views import *

urlpatterns = [
    # url(r'^admin/', admin.site.urls),

    url(r"^register$",RegisterAPI.as_view(),name="register"),
    url(r"^login",my_login,name="login"),
    url(r"^index",index,name="index"),
    url(r"^delete_user",delete_user,name="delete_user"),
    url(r"^update_user",update_user,name="update_user"),
    url(r"^blog",blog,name="blog"),
    url(r"^delete_blog",delete_blog,name="delete_blog"),
    url(r"^get_users_collections/",get_users_collections,name="get_users_collections"),
    url(r"^get_blogs/",get_blogs,name="get_blogs"),
    url(r"^update_blog/",update_blog,name="update_blog"),
    url(r"^create_collections/",create_collections,name="create_collections")
    # url(r"^check_uname$",check_uname,name="check_uname"),
    # url(r"^check_upwd$",check_upwd,name="check_upwd")
]
