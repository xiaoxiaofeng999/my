# 存放自定义的模板标签代码。
from ..models import Article,Tag,Category
from django import template
# 获取最新文章
register = template.Library()  # 实例化一个template.Library类，调用装饰器

@register.simple_tag()
def get_recent_article(num=5):
    return Article.objects.all().order_by('created_time')[:num]

def get_all_tags():
    return Tag.objects.all()

@register.simple_tag()
def get_all_category():
    return Category.objects.all()











