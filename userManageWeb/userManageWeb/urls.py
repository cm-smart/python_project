"""
URL configuration for userManageWeb project.

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
    # 部门管理
    path('department/list/', views.department_list),
    path('department/add/',views.department_add),
    path('department/delete/',views.department_delete),
    path('department/<int:id>/edit/',views.department_edit),

    # 用户管理
    path('userInfo/list/',views.userInfo_list),
    path('userInfo/add/',views.userInfo_add),
    path('userInfo/modelForm/add/',views.userInfo_modelForm_add),

    path('testAjax/',views.testAjax),
    path('testAjaxGet/',views.testAjaxGet),
    path('testAjaxPost/',views.testAjaxPost),
]
