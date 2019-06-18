
from django.conf.urls import url, include
from django.contrib import admin

# from .views import *
from myapp.views import *

urlpatterns = [
    # url(r'^admin/', admin.site.urls),

    url(r"^register$",RegisterAPI.as_view(),name="register"),
    url(r"^check_uname$",check_uname,name="check_uname"),
    url(r"^check_upwd$",check_upwd,name="check_upwd")
]
