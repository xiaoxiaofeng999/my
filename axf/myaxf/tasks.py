from celery import task
from django.core.mail import send_mail
from django.template import loader
from django.core.cache import caches, cache


from axf import settings
# 获得缓存
cache = caches["confirm"]

@task
def send_verify_mail(url,user_id,reciever):
    print("正在发送邮件")
    title = "红烂漫"
    content = ""
    # 加载页面
    template = loader.get_template("user/email.html")
    # 渲染
    html = template.render({"url":url})
    email_from = settings.DEFAULT_FROM_EMAIL
    send_mail(title,content,email_from,[reciever],html_message=html)

    # 设置缓存
    cache.set(url.split("/")[-1],user_id,settings.VERIFY_CODE_MAX_AGE)