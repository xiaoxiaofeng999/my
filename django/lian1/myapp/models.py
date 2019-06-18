from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(
        max_length=20
    )
    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(
        max_length=20
    )
    author = models.ManyToManyField(
        Author
    )
    def __str__(self):
        return self.name

class MyUser(AbstractUser):
    email = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="邮箱号"
    )
    # 如果是追加的字段 我们需要设置null=True 或者default
