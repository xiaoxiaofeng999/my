import tinymce
from django.contrib.auth.models import AbstractUser
from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class MyUser(AbstractUser):
    phone = models.CharField(
        max_length=13,
        verbose_name="手机号",
        unique=True

    )
    email = models.CharField(
        max_length=130,
        null=True
    )
    age = models.IntegerField(
        null=True
    )
    is_delete = models.BooleanField(
        default=False
    )
    def delete(self, using=None, keep_parents=False):
        # 重写数据库删除方法
        self.is_delete = True
        self.save()

class My_blog(models.Model):
    b_title = models.CharField(
        max_length=70
    )
    b_content =tinymce.models.HTMLField()

    def __str__(self):
        return self.b_title

    user= models.ManyToManyField(
        MyUser,
        null=True
    )