from __future__ import absolute_import
from celery import Celery
from django.conf import settings
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","axf:settings")
app = Celery("mycelery")
app.conf.celery_timezone = "Asia/Shanghai"
app.config_from_object("django.conf:settings")
app.autodiscover_tasks(lambda :
                       settings.INSTALLED_APPS
                       )