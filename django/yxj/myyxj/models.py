from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class MyUser(AbstractUser):
    email = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="邮箱"
    )
    address = models.CharField(
        max_length=255,
        null=True,
        verbose_name="地址"
    )
    phone = models.CharField(
        max_length=20,
        null=True,
        verbose_name="手机号"
    )
    icon = models.ImageField(
        upload_to="icon",
        null=True
    )


class Goods(models.Model):
    productimg = models.CharField(
        max_length=255,
        verbose_name="商品图片"
    )
    productname = models.CharField(
        max_length=100,
        verbose_name="商品名字"
    )
    productgram = models.CharField(
        max_length=10,
        verbose_name="商品克重"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="商品价格"
    )
    originalprice = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="商品原价"
    )
    firsttypeid = models.IntegerField(
        verbose_name="一级分类id"
    )
    secondtypeid = models.IntegerField(
        verbose_name="二级分类id"
    )
    secondtype = models.CharField(
        max_length=30,
        verbose_name="商品二级分类"
    )
    storenums = models.IntegerField(
        default=4000,
        verbose_name="库存",
    )
    salesvolume = models.IntegerField(
        default=300,
        verbose_name="销量",
    )
    productid = models.IntegerField(
        verbose_name="产品编号"
    )


class GoodsType(models.Model):
    typeid = models.CharField(
        max_length=20
    )
    typename = models.CharField(
        max_length=30
    )
    childtypenames = models.CharField(
        max_length=255
    )
    typesort = models.IntegerField()

    class Meta:
        verbose_name = "商品分类"


class Cart(models.Model):
    user = models.ForeignKey(
        MyUser
    )
    goods = models.ForeignKey(
        Goods
    )
    num = models.IntegerField(
        default=1,
        verbose_name="商品数量"
    )
    create_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name="添加时间"
    )
    update_time = models.DateTimeField(
        auto_now=True,
        verbose_name="更新时间"
    )
    is_selected = models.BooleanField(
        default=True,
        verbose_name="选中状态"
    )
    token_id = models.CharField(
        max_length=255,
        verbose_name="唯一标识"
    )

    class Meta:
        verbose_name = "购物车"
        index_together = ["user", "goods"]