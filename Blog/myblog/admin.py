from django.contrib import admin
from .models import *
# Register your models here.

# 自定义一个admin 类
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title"]
    list_per_page = 5


class Mysite(admin.AdminSite):
    site_header = "我的博客"

site = Mysite()
site.register(Article,ArticleAdmin)