from django.db import models

# Create your models here.

# 自动创建表app01_userinfo
class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    pwd = models.CharField(max_length=64)
    age = models.IntegerField()
    # 新增设置默认值
    # sex = models.IntegerField(default=1)
    # 允许为空
    # data = models.IntegerField(null=True,blank=True)

class Department(models.Model):
    title = models.CharField(max_length=16)


