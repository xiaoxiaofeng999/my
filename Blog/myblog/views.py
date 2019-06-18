from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, render_to_response
from myblog.models import *
import json
# Create your views here.

def my_home(req):
    allcategory = Category.objects.all()
    allarticle = Article.objects.all()
    allarticle = allarticle.order_by('-id')[0:5]
    hot = Article.objects.all().order_by("-record")[:10] # 通过浏览数进行排序
    tags = Tag.objects.all()
    context = {
        'allcategory': allcategory,
        "allarticle": allarticle,
        'hot':hot,
        'tags':tags
    }
    return render(req, 'home.html',context)

#内容页
def detail(req,id):
    allarticle = Article.objects.all()
    try:
        show = allarticle.get(id=id) # 查询指定id 的文章
        show.record = show.record + 1
        show.save()
    except Exception:
        raise Http404
    allcategory = Category.objects.all()
    try:
        previous_blog = allarticle.filter(created_time=show.created_time,category_id=show.category.id).first()
        next_blog =allarticle.filter(created_time__lt=show.created_time,category_id=show.category.id).last()
    except Exception:
        raise Http404
    content={
        "show":show,
        "allcategory":allcategory,
        "previous_blog":previous_blog,
        "next_blog":next_blog
    }
    # print(show)
    return render(req, 'detail.html', content)

# 搜索页面
def search(req):
    pass
def my_study(req):
    study  = Category.objects.get(id=1)
    study_article = study.article_set.all()
    content = {
        'study_article':study_article
    }
    return  render(req,"my_study.html",content)

def my_suibi(req):
    suibi = Category.objects.get(id=2)
    suibi_article = suibi.article_set.all()
    content = {
        'suibi':suibi,
        'suibi_article':suibi_article
    }
    return  render(req,"my_suibi.html",content)
def my_liuyian(req):
    return  render(req,"my_liuyian.html")

def mine(req):
    return render(req,'mine.html')
