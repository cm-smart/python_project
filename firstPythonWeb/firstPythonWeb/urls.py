"""
URL configuration for firstPythonWeb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # index  -> 寻找views下的index函数
    path('index/', views.index),

    # 用户列表
    path('user/list/',views.user_list),

    path('user/add/',views.user_add),

    path('tpl/',views.tpl),

    path('news/',views.news),

    path('something/',views.something),

    # 用户登录
    path('login/',views.login),

    # orm操作
    path('orm/',views.orm),

    # 案例-用户管理
    # 列表展示
    path('userInfo/list/',views.userInfo_list),
    # 添加
    path('userInfo/add/',views.userInfo_add),
    # 删除
    path('userInfo/delete/',views.userInfo_delete),

]
