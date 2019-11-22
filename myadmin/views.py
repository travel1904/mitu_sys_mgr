from django.http import HttpRequest
from django.shortcuts import render, redirect
from common import make_pwd
from myadmin.models import SysUser


def index_view(request: HttpRequest):
	return render(request, 'index.html')


def to_login(request: HttpRequest):
    if request.method == "POST":
        # 获取用户名和口令
        name = request.POST.get('username', '')
        pwd = request.POST.get('password', '')
        print(name,pwd)
        if any((not name, not pwd, len(name) == 0, len(pwd) == 0)):
            error = '用户名或密码不能为空!'
        else:
            ret = SysUser.objects.filter(name=name, auth_string=make_pwd(pwd))
            if ret.exists():
                login_user = ret.first()

                # 将登录的用户信息存在session中
                request.session['login_user'] = {
                    'id': login_user.id,
                    'name': login_user.name,
                    'role_name': login_user.role.name,
                    'role_code': login_user.role.code
                }

                return redirect('/')

            error = "用户名或密码错误!"

    return render(request, 'login.html', locals())


# def regist_view(request: HttpRequest):
# 	return render(request, 'register.html')


def logout_view(request: HttpRequest):
    request.session.pop('login_user')
    return redirect('/login/')