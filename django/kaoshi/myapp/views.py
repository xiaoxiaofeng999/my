import re
from django.contrib.auth import authenticate, login

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from myapp.models import *


class RegisterAPI(View):
    def  get(self,req):
        return render(req,"register/register.html")
    def post(self,req):
        # 解析参数
        params = req.POST
        name = params.get("u_name")
        pwd = params.get("u_pwd")
        confirm_pwd = params.get("u_confirm_pwd")
        phone = params.get("phone")
        # 校验密码格式
        if pwd and confirm_pwd and pwd == confirm_pwd:
#             # 判断用户名是否可用
            if MyUser.objects.filter(username=name).exists():

              return render(req,"register/register.html",{"help_msg":"该用户已经存在"})
            else:
                user = MyUser.objects.create_user(
                    username=name,
                    password=pwd,
                    phone=phone,
                )
                data = {
                    "code": 1,
                    "msg": "注册成功",
                    "data": "/myapp/login"
                }
                return JsonResponse(data)


def check_uname(req):
    # 解析参数
    uname = req.GET.get("u_name")
    # 判断数据不能是空白，然后去搜索用户
    data = {
        "code": 1,
        "data": ""
    }
    if uname and len(uname) >= 6:
        if MyUser.objects.filter(username=uname).exists():
            data["msg"] = "账号已存在"
        else:
            data['msg'] = "账号可用"
    else:
        data["msg"] = "用户名至少6位"

    return JsonResponse(data)

# def check_upwd(req):
#     # 解析参数
#     pwd = req.GET.get("u_pwd")
#     print(pwd)
#     # 判断数据不能是空白，然后去搜索用户
#     data = {
#         "code": '',
#         "data": ""
#     }
#     pwd = str(pwd)
#     r1 = "^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,10}$" # 强密码(必须包含大小写字母和数字的组合，不能使用特殊字符，长度在8-10之间)
#     # if pwd and len(pwd) >= 6:
#
#     if len(pwd)> 6:
#
#         if  re.search(r1,pwd)==None:
#             data["msg"] = "密码必须包含数字、大小写英文字母"
#             data["code"] = 2
#             print("密码必须包含数字、大小写英文字母")
#         else:
#             data["msg"] = ""
#             data["code"] = 1
#             print("kong")
#     else:
#         data["msg"] = "密码不小于6位"
#         data["code"] = 3
#         print("不小于6")
#         # else:
#         #     data['msg'] = ""
#
#
#     return JsonResponse(data)

# 登录

def my_login(req):
    if req.method == "GET":
        return render(req,"login/login.html")
    else:
        params = req.POST
        user_info = params.get("user_info")
        pwd = params.get("pwd")
        # 认证
        user = authenticate(username = user_info,password = pwd)
        # 判断是否校验成功

        if user :
            # 判断用户的is_delete属性，如果没有删除，属性为False,删除了就是True,不通过
            if user.is_delete == False:
                login(req,user)
                data = {
                    "code": 1,
                    "msg": "登录成功",
                    "data": ""
                }
                return JsonResponse(data)
                # return HttpResponse("登录成功")
            else:
                data = {
                    "code": 2,
                    "msg": "该用户已经不存在了，请重新注册",
                    "data": ""
                }
                return JsonResponse(data)
                # return HttpResponse("该用户已经不存在了，请重新注册")
        else:
            data = {
                "code": 3,
                "msg": "没有用户",
                "data": ""
            }
            return JsonResponse(data)
            # return HttpResponse("登录失败")

def index(req):
    return render(req,"index/index.html")

# http://47.99.193.48:8000/myapp/delete_user?u_id=6
# 删除用户
def delete_user(req):
    # 解析参数
    param = req.GET
    u_id = param.get("u_id")
    u_id = int(u_id)
    # 查到该用户
    try:
        u = MyUser.objects.get(pk=u_id)
        u.delete()
        data = {
            "code": 1,
            "msg": "删除成功",
            "data": ""
        }
        return JsonResponse(data)
        # return HttpResponse("删除成功")
    except Exception:
        data = {
            "code": 2,
            "msg": "没有该数据",
            "data": ""
        }
        return JsonResponse(data)
        # return HttpResponse("没有该数据")

# 用户信息的修改,只修改手机号码
  # 拿到用户id，判断是否有用户，找出用户对象，
# 因为是以手机号注册的，手机号不能重复，得要判断手机号的唯一性,并且得做手机号的正则验证
def update_user(req):
    if req.method == "GET":
        return render(req, "users/user.html")
    else:
        data = {
            "data": ""
        }
        params = req.POST
        users_id = params.get("users_id")
        new_info = params.get("new_info")
        if users_id and new_info:
            users_id = int(users_id)
            try:
                u = MyUser.objects.get(id=users_id)
                if not MyUser.objects.filter(phone=new_info).exists():
                    u.phone = new_info
                    u.save()
                    data["msg"] = "修改成功"
                    data["code"] = "1"
                    return JsonResponse(data)
                    # return HttpResponse("修改成功")
                else:
                    data["msg"] = "该手机号已存在"
                    data["code"] = "2"
                    return JsonResponse(data)
                    # return HttpResponse("该手机号已存在")
            except Exception:
                data["msg"] = "没有该用户"
                data["code"] = "3"
                return JsonResponse(data)
                # return HttpResponse("没有该用户")
        else:
            data["msg"] = "请输入..."
            data["code"] = "4"
            # return HttpResponse("请输入...")
            return JsonResponse(data)



# 创建博客
def blog(req):
    if req.method == "GET":
        return render(req,"blog/blog.html")
    else:
        # 解析参数
        params = req.POST
        title = params.get("title")
        content = params.get("content")
        # 创建博客
        blog = My_blog.objects.create(
            b_title = title,
            b_content = content
        )
        data = {
            "code": 1,
            "msg": "成功创建博客",
            "data": ""
        }
        return JsonResponse(data)
        # return HttpResponse("成功创建博客{}".format(blog.b_title))

def update_blog(req):
    if req.method == "GET":
        return render(req, "blog/update_blog.html")
    else:
        data = {
            "data": ""
        }
        params = req.POST
        blog_id = params.get("blog_id")
        title = params.get("title")
        if blog_id and title:
            blog_id = int(blog_id)
            try:
                blog = My_blog.objects.get(id=blog_id)

                blog.title = title
                blog.save()
                data["msg"] = "修改成功"
                data["code"] = "1"
                return JsonResponse(data)
                    # return HttpResponse("修改成功")
            except Exception:
                data["msg"] = "没有该博客"
                data["code"] = "3"
                return JsonResponse(data)
                # return HttpResponse("没有该用户")
        else:
            data["msg"] = "请输入..."
            data["code"] = "4"
            # return HttpResponse("请输入...")
            return JsonResponse(data)

def delete_blog(req):
    # 解析参数
    param = req.GET
    b_id = param.get("b_id")
    b_id = int(b_id)
    # 查到该博客
    try:
        b = My_blog.objects.get(pk=b_id)
        b.delete()
        data = {
            "code": 1,
            "msg": "删除成功",
            "data": ""
        }
        return JsonResponse(data)
        # return HttpResponse("删除成功")
    except Exception:
        data = {
            "code": 2,
            "msg": "没有该博客",
            "data": ""
        }
        return JsonResponse(data)

# user是写在blog里面
# t通过博客获得用户
def get_users_collections(req):
    if req.method == "GET":
        return render(req,"collect/collect.html")
    else:
        params = req.POST # 获得博客的id
        blog_id = params.get("blog_id")
        blog_id = int(blog_id)
        try:
        # 通过博客的id去博客表里匹配 ，查找出博客对象
            blogs = My_blog.objects.get(id=blog_id)
        # 通过正向关系查找收藏该博客的用户
            users = blogs.user.all()
            print(users)
            data = {
                "code": 1,
                "msg": "有用户收藏了该博客，查询成功",
                "data": ""
            }
            return JsonResponse(data)
            # return HttpResponse("ok")
        except Exception:
            data = {
                "code": 2,
                "msg": "没有该博客，或者没有被收藏",
                "data": ""
            }
            return JsonResponse(data)

def get_blogs(req):
    if req.method == "GET":
        return render(req,"collect/blogs.html")
    else:
        params = req.POST # 获得用户的id
        users_id = params.get("users_id")
        users_id = int(users_id)
        print(users_id)
        # 先判断该用户是否存在，存在再去查收藏，判断是否有收藏，不存在返回失败
        try:
            users = MyUser.objects.get(id=users_id)

            # 通过映射关系查找用户收藏的博客
            print(users)
            blogs = users.my_blog_set.all()
            print(blogs)
            if blogs:
                data = {
                    "code": 1,
                    "msg": "查询成功",
                    "data": ""
                }
                return JsonResponse(data)
            else:
                data = {
                    "code": 2,
                    "msg": "该用户没有收藏",
                    "data": ""
                }
                return JsonResponse(data)
        except Exception:
            data = {
                "code": 3,
                "msg": "没有该用户",
                "data": ""
            }
            return JsonResponse(data)
#1.解析参数，找到用户id,判断用户是否存在，
# （最好有一个选项框，将博客列出来，用户选择，后台接收到选的哪个博客，）
# 2.找到该用户 和博客
# 3.该博客添加到用户表中）
def create_collections(req):
    if req.method == "GET":
        return render(req,"users/user_collect.html")
    else:
        # 解析参数
        params = req.POST
        user_name = params.get("user_name")
        blog_id = params.get("blog_id")
        # 创建收藏
        if user_name and blog_id:
            if  MyUser.objects.filter(username=user_name).exists():

                u = MyUser.objects.get(username=user_name)
                blog = My_blog.objects.get(id=blog_id)
                blog = My_blog.objects.create(
                    user = u.id
                    )
                return HttpResponse("ok")
            else:
                return HttpResponse("用户不存在")
        else:
            return HttpResponse("请输入...")
