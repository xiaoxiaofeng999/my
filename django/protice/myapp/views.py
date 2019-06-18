from django.core.serializers import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
import json
# Create your views here.
from myapp.models import Student, Grade, Book, Author


# z知道学生查出成绩（学生的外键是班级）
def get_grade(req):
    stu = Student.objects.get(id=1)

    return HttpResponse(stu.grade.score)
# 通过grade拿学生信息
def get_student(req):
    grade = Grade.objects.get(id=1)
    stu = grade.student_set.all()
    # print(stu)
    return HttpResponse(stu)

# 多对多关系，外键写在book中

def get_author(req):
    # 通过书本获取作者
    try:
        book = Book.objects.get(pk=3)
        res = book.author.all()
        print(book)
    except Exception:
        return HttpResponse("找不到")
    return HttpResponse(res)

def get_book(req):
    author = Author.objects.all()
    print('A')
    for i in author:
        print(i)
    return HttpResponse('ok')


def json_test(req):
    author = Author.objects.all()
    data = {
        "code":1,
        "msg":"hehe",
        "data":author
    }
    return JsonResponse(data)