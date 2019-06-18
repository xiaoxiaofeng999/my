from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
# 自定义用户
class MyUser(AbstractUser):
    email = models.CharField(
        max_length= 100,
        unique=True,
        verbose_name="邮箱"

    )
    address = models.CharField(
        max_length=251,
        verbose_name= "地址",
        null = True
    )
    phone = models.CharField(
        max_length=13,
        verbose_name="手机号",
        null = True
    )
    icon = models.ImageField(
        upload_to="icons" , # 指定文件保存的路径名 系统自动创建
        null = True
    )

class BaseData(models.Model):
    img = models.CharField(
        max_length=251
    )
    name = models.CharField(
        max_length=40
    )
    trackid = models.CharField(
        max_length=30
    )
    class Meta:
        abstract = True

class Wheel(BaseData):
    class Meta:
        db_table = "axf_wheel"

class Nav(BaseData):
    class Meta:
        db_table="axf_nav"

class MustBuy(BaseData):
    class Meta:
        db_table = "axf_mustbuy"

class Shop(BaseData):
    class Meta:
        db_table ="axf_shop"
class MainShow(BaseData):
    categoryid = models.CharField(
        max_length=10
    )
    brandname = models.CharField(
        max_length=20
    )
    img1 = models.CharField(
        max_length=255
    )
    childcid1 = models.CharField(
        max_length=10
    )
    productid1 = models.CharField(
        max_length=10
    )
    longname1 = models.CharField(
        max_length=40
    )
    price1 = models.CharField(
        max_length=10
    )
    marketprice1 = models.CharField(
        max_length=10
    )



    img2 = models.CharField(
        max_length=255
    )
    childcid2 = models.CharField(
        max_length=10
    )
    productid2 = models.CharField(
        max_length=10
    )
    longname2 = models.CharField(
        max_length=40
    )
    price2 = models.CharField(
        max_length=10
    )
    marketprice2 = models.CharField(
        max_length=10
    )

    img3 = models.CharField(
        max_length=255
    )
    childcid3 = models.CharField(
        max_length=10
    )
    productid3 = models.CharField(
        max_length=10
    )
    longname3 = models.CharField(
        max_length=40
    )
    price3 = models.CharField(
        max_length=10
    )
    marketprice3 = models.CharField(
        max_length=10
    )

    class Meta:
        db_table = "axf_mainshow"

class FoodTypes(models.Model):
    typeid = models.CharField(
        max_length=20
    )
    typename = models.CharField(
        max_length= 30
    )
    childtypenames = models.CharField(
        max_length=255
    )
    typesort = models.IntegerField()
    class Meta:
        db_table = "axf_foodtypes"

class Goods(models.Model):
    productid = models.CharField(
        max_length=20
    )
    productimg = models.CharField(
        max_length=255
    )
    productname = models.CharField(
        max_length=130
    )
    productlongname = models.CharField(
        max_length = 190
)
    isxf = models.BooleanField(
        default=0
    )
    pmdesc = models.IntegerField()
    specifics = models.CharField(
        max_length =40
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places = 2
    )
    marketprice = models.DecimalField(
        max_digits=10,
        decimal_places = 2
    )
    categoryid = models.IntegerField()
    childcid = models.IntegerField(
    )
    childcidname = models.CharField(
    max_length = 30
    )
    dealerid = models.CharField(
    max_length = 30
    )
    storenums = models.IntegerField(
    verbose_name = "库存"
    )
    productnum = models.IntegerField(
    verbose_name = "销量"
    )

    class Meta:
        db_table = "axf_goods"

class Cart(models.Model):
    user = models.ForeignKey(
        MyUser
    )
    goods = models.ForeignKey(
        Goods
    )
    num = models.IntegerField(
        default=1
    )
    create_time = models.DateTimeField(
        auto_now_add=True
    )
    update_time = models.DateTimeField(
        auto_now= True

    )
    is_selected = models.BooleanField(
        default=True
    )
    class Meta:
        verbose_name = "购物车"
        index_together = ["user","goods"]

class MineBtnS1(models.Model):
    btn = models.CharField(
        max_length=30
    )
    class_name = models.CharField(
        max_length=140
    )
    bref_url = models.CharField(
        max_length=255,
        null=True
    )
    is_used = models.BooleanField(
        default=True
    )

    class Meta:
        verbose_name = "我的页面的上一排按钮"
# 我的页面按钮
class MineBtnS(models.Model):
    btn = models.CharField(
        max_length=30
    )
    class_name = models.CharField(
        max_length=140
    )
    bref_url = models.CharField(
        max_length=255,
        null=True
    )
    is_used = models.BooleanField(
        default=True
    )
    class Meta:
        verbose_name="我的页面的下一排按钮"


class IDCardv1(models.Model):
    num = models.CharField(
        max_length=20
    )
    addr = models.CharField(
        max_length=20
    )
class People(models.Model):
    name=models.CharField(
        max_length=30
    )
    age = models.IntegerField(default=10)
    idcard = models.OneToOneField(
        IDCardv1
    )

class Order(models.Model):
    ORDER_STATUS = (
        (1,"代付款"),
        (2,"已付款"),
        (3,"已发货"),
        (4,"已收货"),
        (5,"待评价"),
        (6,"已评价")
    )
    user = models.ForeignKey(
        MyUser
    )
    create_time = models.DateTimeField(
        auto_now_add=True
    )
    status = models.IntegerField(
        choices =ORDER_STATUS,
        default=1
    )
# 订单详情
class OrderItem(models.Model):
    order = models.ForeignKey(
        Order
    )
    goods = models.ForeignKey(
        Goods
    )
    num = models.IntegerField(
        verbose_name="数量"
    )
    buy_money = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

class VIP(models.Model):
    user = models.ForeignKey(
        MyUser
    )
    desc = models.CharField(
        default="爱鲜蜂黄钻",
        max_length=50
    )
    is_active = models.BooleanField(
        default=True
    )
