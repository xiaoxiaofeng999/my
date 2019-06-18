from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r"^index",IndexAPI.as_view(),name="index"),
    url(r"^prodectlist/(\d+)/(\d+)",prodectlist,name="prodectlist"),
    url(r"^register$",RegisterAPI.as_view(),name='register'),
    url(r"^login$",LoginAPI.as_view(),name='login'),
    url(r"^login$",LoginAPI.as_view(),name='login'),
    url(r"^ProductDetails/(\d+)$",ProductDetails,name='ProductDetails'),
    url(r"^cart$",CartAPI.as_view(),name='cart'),
]