import json
import time

from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect

from app01 import models
from app01.models import Department, UserInfo

from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def department_list(request):

    # 从数据库中获取数据
    data_list = Department.objects.all()

    return render(request,'department_list.html',{'data_list':data_list})

def department_add(request):
    print(request.method)
    if request.method == 'GET':
        return render(request, 'department_add.html')

    title = request.POST.get('title')
    # 添加到数据库
    Department.objects.create(title=title)

    return redirect("/department/list/")

def department_delete(request):
    id = request.GET.get('id')
    # 数据库删除
    Department.objects.filter(id=id).delete()

    return redirect("/department/list/")

# /department/1/edit
def department_edit(request,id):
    if request.method == 'GET':
        # 根据id获取数据
        obj = Department.objects.filter(id=id).first()

        return render(request,'department_edit.html',{'obj':obj})

    title = request.POST.get('title')

    # 修改数据库
    Department.objects.filter(id=id).update(title=title)

    return redirect("/department/list/")

def userInfo_list(request):
    # 从数据库获取数据
    data_list = UserInfo.objects.all()

    return render(request,'userInfo_list.html',{'data_list':data_list})

def userInfo_add(request):

    if request.method == 'GET':
        depart_list = Department.objects.all()
        print(depart_list)
        context = {
            'sex_choices': UserInfo.sex_choices,
            'depart_list': depart_list
        }
        return render(request,'userInfo_add.html',context)

    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    age = request.POST.get('age')
    account = request.POST.get('account')
    sex = request.POST.get('sex')
    depart_id = request.POST.get('depart_id')
    date = time.strftime("%Y-%m-%d", time.localtime())

    # 添加到数据库
    UserInfo.objects.create(name=name,pwd=pwd,age=age,account=account,sex=sex,depart_id=depart_id,create_time=date)

    return redirect('/userInfo/list/')

class UserModelForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ["name","pwd","age","account","sex","create_time","depart"]
        # widgets = {
        #     "name":forms.TextInput(attrs={"class":"form-control"}),
        #     "pwd":forms.TextInput(attrs={"class":"form-control"}),
        #     "age":forms.TextInput(attrs={"class":"form-control"}),
        #     "account":forms.TextInput(attrs={"class":"form-control"}),
        #     "create_time":forms.TextInput(attrs={"class":"form-control"}),
        #     "sex":forms.Select(attrs={"class":"form-control"}),
        #     "depart":forms.Select(attrs={"class":"form-control"})
        # }
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs = {"class":"form-control"}

def userInfo_modelForm_add(request):
    """添加用户，使用modelForm"""
    if request.method == 'GET':
        form = UserModelForm()
        return render(request,'userInfo_modelForm_add.html',{'form':form})
    # post提交
    form = UserModelForm(data=request.POST)
    if form.is_valid():
        print(form.cleaned_data)
    else:
        print(form.errors)

    return redirect('/userInfo/list/')


# 测试ajax请求
def testAjax(request):

    # data = {"name":"chenmin","age":30}
    # json.dumps()将 Python 对象编码成 JSON 字符串
    # json.loads()将已编码的 JSON 字符串解码为 Python 对象
    # data_str = json.dumps(data)

    return render(request,'ajax_test.html')

def testAjaxGet(request):
    name = request.GET.get("name")
    age = request.GET.get("age")

    data = {"name":name,"age":age}
    data_str = json.dumps(data)

    return HttpResponse(data_str)

@csrf_exempt
def testAjaxPost(request):
    name = request.POST.get("name")
    age = request.POST.get("age")

    data = {"name": name, "age": age}
    data_str = json.dumps(data)

    return HttpResponse(data_str)