import json

from django.http import HttpResponse,JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from myapp.models import Book, Author, MyUser


def get_author(req):
    # 通过书拿作者
    book = Book.objects.get(id=3)

    res = book.author.all()
    res = book.author.filter(name="鲁迅")
    print(res)
    return HttpResponse('ok')

def get_book(req):
    author = Author.objects.get(id=1)

    res = author.book_set.filter(name__contains= "骆驼")
    print(res)
    return HttpResponse("ok")


def json_test(req):
    data = {
        "code":1,
        "msg":"hehe",
        "data":[1,2,3,4]
    }
    json_str = json.dumps(data)
    json_data = json.loads(json_str)
    # return JsonResponse(data)
    print("host",req.get_host())
    return HttpResponse(json_data)

def test_res(req):
    response = HttpResponse()
    response.status_code = 202
    response.content = "HAHAHA"
    return response


class Register(View):
    def get(self,req):
        return render(req,'register/register.html')
    def post(self,req):
        # 解析参数
        params = req.POST
        name = params.get("u_name")
        email = params.get("email")
        pwd = params.get("pwd")
        confirm_pwd = params.get("confirm_pwd")
        # 校验密码
        if pwd and confirm_pwd and pwd == confirm_pwd:
            #             # 判断用户名是否可用
            if MyUser.objects.filter(username=name).exists():
                return render(req, "register/register.html", {"help_msg": "该用户已经存在"})
            else:
                user = MyUser.objects.create_user(
                    username=name,
                    password=pwd,
                    email=email,
                    is_active=False,
                )
                return render(req,"login/login.html")














