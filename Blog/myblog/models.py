from DjangoUeditor3.DjangoUeditor.models import UEditorField
from django.db import models
# Create your models here.
import tinymce
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class MyUser(AbstractUser):
    email = models.CharField(
        max_length=40,
        null=True,
        verbose_name="邮箱"
    )
    icon = models.ImageField(
        null = True,
        upload_to="icons"
    )

# 博客分类模型
class Category(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="分类名"
    )
    class Meta:
        verbose_name ="博客分类"
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(
        max_length=40,
        null=True,
        verbose_name="标签云"
    )
    def __str__(self):
        return  self.name
    class Meta:
        verbose_name = "标签云"

# 建立文章模型

class Article(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="标题",
    )
    content = UEditorField(
        blank=True,
        null=True,
        verbose_name="文章内容",
        width=800,
        height=500,
        toolbars="full",
        imagePath="upimg/",
        filePath="upfile/",
        upload_settings={"imageMaxSize": 1204000},
        settings={},
        command=None,
    )
    # img = models.ImageField(
    #     verbose_name="文章封面图片",
    #     null=True
    #
    # )
    created_time = models.DateTimeField(
        verbose_name="发布时间",
        auto_now_add=True,
        null=True
    )
    update_date = models.DateTimeField(
        auto_now=True,
        verbose_name="更新时间",
        null=True
    )
    category = models.ForeignKey(
        Category,
        null=True
    )
    # 浏览
    record = models.PositiveIntegerField(
        default=0,
        verbose_name="浏览"
    )
    tag = models.ManyToManyField(
        Tag,

    )
    user = models.ForeignKey(
        MyUser,
        null=True
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "博客文章"

#Banner
class Banner(models.Model):
    text_info = models.CharField('标题', max_length=50, default='')
    img = models.ImageField('轮播图', upload_to='banner/',null=True)
    link_url = models.URLField('图片链接', max_length=250)
    is_active = models.BooleanField('是否是active', default=False)

    def __str__(self):
        return self.text_info

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = '轮播图'