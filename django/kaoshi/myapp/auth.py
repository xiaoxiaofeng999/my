from django.contrib.auth.backends import ModelBackend

from .models import MyUser


class MyBackend(ModelBackend):
  def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # username=username 前面这个username 是模型的属性 后面的username是参数
            user = MyUser.objects.get(username=username)
        #     常用异常处理的基类
        except Exception:
            try:
                # 下边的username是这是函数的使用者相当于self,us一个参数ername是
                # phone= username 前面的phone是模型中的属性，后面的username是参数
                user = MyUser.objects.get(phone=username)
            except Exception:
                return None
        # 密码认证:
        if user.check_password(password):
            return user
        else:
            return None