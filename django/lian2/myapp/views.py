import re
from django.http import JsonResponse

from django.shortcuts import render

# Create your views here.
from django.views import View

from myapp.models import MyUser

class RegisterAPI(View):

    def get(self, req):
        return render(req, "register/register.html")

    def post(self, req):
        # 解析参数
        params = req.POST
        name = params.get("uname")
        pwd = params.get("u_pwd")
        confirm_pwd = params.get("u_confirm_pwd")
        email = params.get("email")
        # 校验密码
        if pwd and confirm_pwd and pwd == confirm_pwd:
            # 判断用户名是否可用
            if MyUser.objects.filter(username=name).exists():
                return render(req, "register/register.html", {"help_msg": "该用户已存在"})
            else:
                user = MyUser.objects.create_user(
                    username=name,
                    password=pwd,
                    email=email,


                )

                return render(req, "login/login.html")



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

def check_upwd(req):
    # 解析参数
    pwd = req.GET.get("u_pwd")
    print(pwd)
    # 判断数据不能是空白，然后去搜索用户
    data = {
        "code": '',
        "data": ""
    }
    pwd = str(pwd)
    r1 = "^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,10}$" # 强密码(必须包含大小写字母和数字的组合，不能使用特殊字符，长度在8-10之间)
    # if pwd and len(pwd) >= 6:

    if len(pwd)> 6:

        if  re.search(r1,pwd)==None:
            data["msg"] = "密码必须包含数字、大小写英文字母"
            data["code"] = 2
            print("密码必须包含数字、大小写英文字母")
        else:
            data["msg"] = ""
            data["code"] = 1
            print("kong")
    else:
        data["msg"] = "密码不小于6位"
        data["code"] = 3
        print("不小于6")
        # else:
        #     data['msg'] = ""


    return JsonResponse(data)