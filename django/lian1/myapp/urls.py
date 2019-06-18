
from django.conf.urls import url, include
from django.contrib import admin

# from .views import *
from myapp.views import *

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r"^get_author$",get_author),
    url(r"^get_book$",get_book),
    url(r"^json_test",json_test),
    url(r"^test_res$",test_res),
    url(r"^register$",Register.as_view(),name="register")
]
