from django.shortcuts import render
from MyApp.models import *
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def welcome(request):
    # print("进网站了")
    # return  HttpResponse("欢迎来到首页")
    return  render(request,"welcome.html")


def child(request,eid,oid):
    return render(request,eid)



# 登录
def login(request):
    return render(request,'login.html')

#开始登录
def login_action(request):
    u_name = request.GET['username']
    p_word =request.GET['password']
    #开始连通django 用户库 查看用户名密码是否正确
    print(u_name,p_word)
    from django.contrib import auth
    user = auth.authenticate(username=u_name,password=p_word)
    if user is not None:
        # return HttpResponseRedirect('/home/')
        auth.login(request,user)
        request.session['user']=u_name
        return HttpResponse('成功')
    else:
        #返回前端告诉前端用户名/密码不对
        return HttpResponse('')


