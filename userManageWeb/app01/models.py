from django.db import models

# Create your models here.

class Department(models.Model):
    """部门表"""
    title = models.CharField(verbose_name='标题',max_length=32)

    def __str__(self):
        return self.title

class UserInfo(models.Model):
    """员工表"""
    name = models.CharField(verbose_name="姓名：",max_length=16)
    pwd = models.CharField(verbose_name="密码",max_length=64)
    age = models.IntegerField(verbose_name="年龄")
    account = models.DecimalField(verbose_name="账户余额",max_digits=10,decimal_places=2,default=0)
    create_time = models.DateTimeField(verbose_name="创建时间")

    # 无约束
    # depart_id = models.BigIntegerField(verbose_name='部门id')

    # 有约束
    # - to,与那张表关联
    # 生成数据列 depart_id
    # 级联删除：on_delete=models.CASCADE()
    depart = models.ForeignKey(verbose_name="部门",to="Department",to_field="id",on_delete=models.CASCADE)

    # 在django中做的约束
    sex_choices = (
        (1,'男'),
        (2,'女'),
    )
    sex = models.SmallIntegerField(verbose_name="性别",choices=sex_choices)


