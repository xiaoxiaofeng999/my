# from celery import task
# from django.conf import settings
# from django.core.mail import send_mail
# from django.template import loader
# from django.core.cache import caches
#
#
# # 获取缓存
# cache = caches["confirm"]
#
# @task
#
# def send_verify_email(url, user_id, reciever):
#     title = "邮件验证"
#     content = ""
#     # 加载页面
#     template = loader.get_template("user/sendemail.html")
#     html = template.render({"url":url})
#     email_from = settings.DEFAULT_FROM_EMAIL
#     # 发送邮件
#     send_mail(title, content, email_from, [reciever], html_message=html)
#     # 设置缓存
#     cache.set(url.split("/")[-1], user_id,settings.VERIFY_CODE_MAX_AGE)