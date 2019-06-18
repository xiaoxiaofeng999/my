from django.db import models

# Create your models here.
class IdCard(models.Model):
    num = models.CharField(
        max_length=20,
        verbose_name="身份证编号"
    )
    addr = models.CharField(
        max_length=20,
        default="千锋派出所"
    )
    class Meta:
        verbose_name="身份证类"


class Person(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="人名"
    )
    idcard = models.OneToOneField(
        IdCard
    )

class Grade(models.Model):
    score = models.IntegerField(
        default=0
    )


# Student是多关系，外键是一关系
class Student(models.Model):
    name = models.CharField(
        max_length=30
    )
    grade = models.ForeignKey(
        Grade,
        null=True
    )


class Author(models.Model):
    name = models.CharField(
        max_length=30
    )
    # 重写
    def __str__(self):

        return  self.name

class Book(models.Model):
    name = models.CharField(
        max_length=30
    )
    author = models.ManyToManyField(
        Author
    )
    def __str__(self):
        return self.name

