import hashlib
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import AnonymousUser
from django.core.cache import caches
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
import uuid
# from .tasks import send_verify_email
# from .my_utils import *
from .models import *


# Create your views here.
# cache = caches["confirm"]

class IndexAPI(View):
    def get(self, req):
        user = req.user
        is_login = True
        if isinstance(user, AnonymousUser):
            is_login = False
        u_name = user.username if is_login else ""
        # 获取一级分类
        types = GoodsType.objects.all()
        result = {
            "title": "首页",
            "is_login": is_login,
            "u_name": u_name,
            "firsttypes": types,
        }
        return render(req, "home/index.html", result)

    def post(self, req):
        type_id = req.POST.get("c_id")
        types = GoodsType.objects.all()
        tmp = types.filter(typeid=type_id)[0]
        childtypenames = tmp.childtypenames.split("#")
        secondtypes = [i.split(":") for i in childtypenames]
        print(secondtypes)
        res = {
            "code": 1,
            "msg": "ok",
            "data": secondtypes

        }
        return JsonResponse(res)


def prodectlist(req, type_id, order_type):
    # 一级分类商品
    onetype_id = GoodsType.objects.get(typeid=int(type_id))
    goods = Goods.objects.filter(firsttypeid=onetype_id.typeid)
    twotypeid = req.GET.get("secondtype")
    if twotypeid:
        goods = goods.filter(secondtypeid=twotypeid)
    if int(order_type) == 0:
        goods = goods.order_by("price")
    elif int(order_type) == 1:
        goods = goods.order_by("salesvolume")
    else:
        pass
    result = {
        "title": "商品列表",
        "goods": goods,
        "order_type": int(order_type),
        "one_type_id": int(type_id),
        "twotypeid": twotypeid
    }
    return render(req, "market/productlist.html", result)


def ProductDetails(req, prodect_id):
    # 获取对应的产品
    goods = Goods.objects.filter(productid=int(prodect_id))
    # 一级分类
    p_id = goods.values("firsttypeid")

    second_goods = GoodsType.objects.filter(typeid=p_id)
    print(second_goods)
    result = {
        "title": "商品详情",
        "goods": goods,
        "second_goods": second_goods
    }
    return render(req, "market/ProductDetails.html", result)


class RegisterAPI(View):
    def get(self, req):
        result = {
            "title": "注册"
        }
        return render(req, "user/register.html", result)

    def post(self, req):
        params = req.POST
        name = params.get("u_name")
        password = params.get("u_password")
        passwordRepeat = params.get("u_passwordRepeat")
        email = params.get("u_email")
        if password and passwordRepeat and password == passwordRepeat:
            if MyUser.objects.filter(username=name).exists():
                return render(req, "user/register.html", {"help_msg": "用户已存在"})
            else:
                MyUser.objects.create_user(
                    username=name,
                    password=password,
                    email=email,
                    is_active=True
                )
                return render(req, 'user/login.html')


class LoginAPI(View):
    def get(self, req):
        result = {
            "title": "登录"
        }
        return render(req, "user/login.html", result)

    def post(self, req):
        params = req.POST
        user = params.get("user")
        # print(user)
        password = params.get("password")
        # print(password)
        if not user or not password:
            return redirect(reverse("yxj:login"))
        # 用户通过用户名，手机号,邮箱以及密码进行验证
        user = authenticate(
            username=user,
            password=password

        )
        if user:
            login(req, user)
            token_id = req.COOKIES.get("token")
            if token_id:
                carts = Cart.objects.filter(token_id=token_id).all()
                for cart in carts:
                    cart.user_id = user.id
            return redirect(reverse("yxj:index"))
        else:
            return render(req, "user/login.html")


class LogoutAPI(View):
    def get(self, req):
        logout(req)
        return redirect(reverse("yxj:index"))


class CartAPI(View):
    def get(self, req):
        result = {
            "title": "购物车"
        }
        return render(req, "cart/shopcart.html", result)

    def post(self, req):
        op_type = req.POST.get("type")
        g_id = req.POST.get("g_id")
        # 获取当前用户
        user = req.user
        # 判断用户是否登录
        if not isinstance(user, MyUser):
            token_id = req.COOKIES.get("token")
            if not token_id:
                uuid_str = str(uuid.uuid4()).encode("utf-8")
                md5 = hashlib.md5()
                token_id = md5.update(uuid_str)
            goods = Goods.objects.get(pk=g_id)
            if op_type == "add":
                goods_num = 1
                # 查看库存
                if goods.storenums > 1:
                    cart_goods = Cart.objects.filter(goods=goods)
                    # 判断商品是不是第一次添加
                    if cart_goods.exists():
                        # Cart.objects.filter(token_id=token_id)
                        cart_item = Cart.objects.get(token_id=token_id)
                        cart_item.num = cart_item.num + 1
                        cart_item.save()
                        goods_num = cart_item.num
                    else:

                        Cart.objects.create(
                            token_id=token_id,
                            goods=goods
                        )
                    data = {
                        "code": 1,
                        "msg": "ok",
                        "goods_num": goods_num
                    }
                    response = JsonResponse(data)
                    response.set_cookie("token","token_id")
                    return response
                else:
                    data = {
                        "code":2,
                        "msg": "库存不足",
                        "data":""
                    }
                    return JsonResponse(data)
            elif op_type == "sub":
                goods_num = 0
                cart_item = Cart.objects.get(
                    token_id=token_id,
                    goods=goods
                )
                cart_item.num -=1
                if cart_item.num == 0:
                    cart_item.delete()
                else:
                    goods_num = cart_item.num
                data = {
                    "code": 1,
                    "msg": "ok",
                    "goods_num": goods_num
                }
                return JsonResponse(data)
        else:
            goods = Goods.objects.get(pk=g_id)
            if op_type == "add":
                goods_num = 1
                # 查看库存
                if goods.storenums > 1:
                    cart_goods = Cart.objects.filter(goods=goods)
                    # 判断商品是不是第一次添加
                    if cart_goods.exists():
                        # Cart.objects.filter(token_id=token_id)
                        cart_item = Cart.objects.filter(goods_id=g_id)
                        cart_item.num = cart_item.num + 1
                        cart_item.save()
                        goods_num = cart_item.num
                    else:

                        Cart.objects.create(
                            user_id=user.id,
                            goods=goods
                        )
                    data = {
                        "code": 1,
                        "msg": "ok",
                        "goods_num": goods_num
                    }
                    return JsonResponse(data)
                else:
                    data = {
                        "code":2,
                        "msg": "库存不足",
                        "data":""
                    }
                    return JsonResponse(data)
            elif op_type == "sub":
                goods_num = 0
                cart_item = Cart.objects.get(
                    user_id=user.id,
                    goods=goods
                )
                cart_item.num -=1
                if cart_item.num == 0:
                    cart_item.delete()
                else:
                    goods_num = cart_item.num
                data = {
                    "code": 1,
                    "msg": "ok",
                    "goods_num": goods_num
                }
                return JsonResponse(data)





