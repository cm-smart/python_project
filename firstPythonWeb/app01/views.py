from django.http import HttpResponse
from django.shortcuts import render, redirect
from app01.models import Department, UserInfo


# Create your views here.

def index(request):
    return HttpResponse("欢迎光临")

def user_list(request):
    # return HttpResponse("用户列表")
    # 去app01下的templates寻找user_list.html
    # 根据app注册顺序，寻找app下的templates目录
    return render(request,'user_list.html')

def user_add(request):
    return HttpResponse("用户添加")

def tpl(request):
    name = '陈敏'
    roles = ['管理员','CEO','保安']
    user_info = {'name':'陈敏杰','salary':20000,'role':'CEO'}

    return render(request,'tpl.html',{'name':name,'roles':roles,'user_info':user_info})

def news(req):
    import requests
    res = requests.get('https://www.189.cn/login/index.do')
    print(res)
    data_list = res.json()
    print(data_list)
    return render(req,'news.html',data_list)

def something(request):
    # request是一个对象，封装了用户发送过来的所有请求相关的数据
    # 获取请求方式
    method = request.method
    print(method)
    # 在url上传递值
    print(request.GET)
    # 通过post传递值
    print(request.POST)

    # return HttpResponse("返回内容")
    # return render(request,'something.html',{'title':'某些请求来了'})

    return redirect("https://www.baidu.com")

def login(request):
    print(request.method)
    if request.method == 'GET':
        return render(request,'login.html')

    name = request.POST.get('name')
    pwd = request.POST['pwd']
    if name == 'root' and pwd == 'cm021035':
        return render(request,'index.html')

    return render(request,'login.html',{'errorMsg':'用户名或密码错误'})

def orm(request):
    # 测试orm操作表中的数据
    # Department.objects.create(title='销售部')
    # Department.objects.create(title='IT部')
    # Department.objects.create(title='运营部')
    # UserInfo.objects.create(name='chenmin',pwd='123',age=30)

    # 删除
    # Department.objects.filter(id=3).delete()
    # UserInfo.objects.all().delete()

    # 获取数据
    # data_list = UserInfo.objects.all()
    # print(data_list)
    # for obj in data_list:
    #     print(obj.id,obj.name,obj.pwd,obj.age)
    #
    # obj = UserInfo.objects.filter(id=1).first()
    # print(obj)

    # 更新数据，先查找，后修改
    UserInfo.objects.all().update(age=999)
    UserInfo.objects.filter(id=1).update(age=20)
    return HttpResponse("成功")

def userInfo_list(request):
    # 获取数据库数据
    data_list = UserInfo.objects.all()
    # 将数据渲染到html中
    return render(request,'userInfo_list.html',{'data_list':data_list})

def userInfo_add(request):
    print(request.method)
    if request.method == 'GET':
        return render(request,'userInfo_add.html')

    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    age = request.POST.get('age')

    # 添加到数据库中
    UserInfo.objects.create(name=name,pwd=pwd,age=age)

    return redirect("/userInfo/list")

def userInfo_delete(request):
    if request.method == 'GET':
        id = request.GET.get("id")

        # 删除数据库
        UserInfo.objects.filter(id=id).delete()

        return redirect('/userInfo/list')
