from django.http import HttpRequest
from django.shortcuts import render, redirect

from myadmin.models import SysUser


def index_view(request: HttpRequest):
	return render(request, 'index.html')


def login_view(request: HttpRequest):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        logname = request.POST.get('logname')
        logpwd = request.POST.get('logpwd')
        print("用户名：",logname)
        try:
            log = SysUser.objects.get(name=logname)
            if log.name == logname and log.auth_string == logpwd:
                response = redirect('/')
                request.session['login_user'] = logname
                response.set_cookie('login_status', 'success')
                return response
            else:
                print("用户名或密码错误！")
                return render(request, 'login.html')
        except:
            print("该用户不存在，请重新输入！")
            return render(request, 'login.html')


def regist_view(request: HttpRequest):
	return render(request, 'register.html')


def logout_view(request: HttpRequest):
    request.session.flush()
    return redirect('/login/')