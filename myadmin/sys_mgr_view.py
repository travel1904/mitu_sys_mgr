from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from myadmin.models import *


class RoleView(View):
    def get(self, request):
        if request.GET.get('id', ''):
            role = SysRole.objects.get(pk=request.GET.get('id'))
            return JsonResponse({
                'id': role.id,
                'name': role.name,
                'code': role.code
            })

        roles = SysRole.objects.all()
        return render(request, 'sys_mgr/role.html', locals())

    def post(self, request):
        print(request.POST)
        id = request.POST.get('role_id', None)  # 注意： form表单页面不建议使用id 字段名
        name = request.POST.get('name')
        code = request.POST.get('code')
        # 验证是否为空(建议:页面上验证是否为空)

        if id:
            # 更新
            role = SysRole.objects.get(pk=id)
            role.name = name
            role.code = code  # 建议不修改code
            role.save()
        else:
            SysRole.objects.create(name=name, code=code)

        return redirect('/role/')

    def delete(self, request):
        role_id = request.GET.get('id')
        role = SysRole.objects.get(pk=role_id)
        role.delete()

        return JsonResponse({
            'status': 0,
            'msg': '删除成功!'
        })


class UserView(View):
    def get(self, request):
        if request.GET.get('id', ''):
            role = UserDetail.objects.get(pk=request.GET.get('id'))
            return JsonResponse({
                'id': role.ud_id,
                'name': role.real_name,
                'img': role.ud_img,
                'gender': role.ud_gender,
                'email': role.ud_email,
                'job': role.ud_job
            })

        roles = UserDetail.objects.all()
        return render(request, 'sys_mgr/user.html', locals())

    def post(self, request):
        print(request.POST)
        id = request.POST.get('ud_id', None)  # 注意： form表单页面不建议使用id 字段名
        print(id)
        real_name = request.POST.get('real_name')
        ud_img = request.POST.get('ud_img')
        ud_gender = request.POST.get('ud_gender')
        ud_email = request.POST.get('ud_email')
        ud_job = request.POST.get('ud_job')
        # 验证是否为空(建议:页面上验证是否为空)

        if id:
            # 更新
            role = UserDetail.objects.get(pk=id)
            role.real_name = real_name
            role.ud_img = ud_img  # 建议不修改code
            role.ud_gender = ud_gender
            role.ud_email = ud_email
            role.ud_job = ud_job
            role.save()
        else:
           UserDetail.objects.create(real_name=real_name, ud_img=ud_img, ud_gender=ud_gender, ud_email=ud_email, ud_job=ud_job)

        return redirect('/user/')

    def delete(self, request):
        role_id = request.GET.get('id')
        role = UserDetail.objects.get(pk=role_id)
        role.delete()

        return JsonResponse({
            'status': 0,
            'msg': '删除成功!'
        })


class AuthorityView(View):
    def get(self, request):
        if request.GET.get('id', ''):
            role = TravelCircle.objects.get(pk=request.GET.get('id'))
            return JsonResponse({
                'id': role.tr_id,
                'picture': role.head_picture,
                'nickname': role.nickname,
                'pic_dis': role.pic_dis
            })

        roles = TravelCircle.objects.all()
        return render(request, 'sys_mgr/authority.html', locals())

    def post(self, request):
        print(request.POST)
        id = request.POST.get('tr_id', None)  # 注意： form表单页面不建议使用id 字段名
        head_picture = request.POST.get('head_picture')
        nickname = request.POST.get('nickname')
        pic_dis = request.POST.get('pic_dis')
        # 验证是否为空(建议:页面上验证是否为空)

        if id:
            # 更新
            role = TravelCircle.objects.get(pk=id)
            role.head_picture = head_picture
            role.nickname = nickname
            role.pic_dis = pic_dis
            role.save()
        else:
           TravelCircle.objects.create(head_picture=head_picture, nickname=nickname, pic_dis=pic_dis)

        return redirect('/authority/')

    def delete(self, request):
        role_id = request.GET.get('id')
        role = TravelCircle.objects.get(pk=role_id)
        role.delete()

        return JsonResponse({
            'status': 0,
            'msg': '删除成功!'
        })


class CaidanView(View):
    def get(self, request):
        if request.GET.get('id', ''):
            role = TravelerInfo.objects.get(pk=request.GET.get('id'))
            return JsonResponse({
                'id': role.travel_id,
                'name': role.name,
                'code': role.gender,
                'card': role.id_card,
                'phone': role.phone_num,
                'date': role.go_date
            })

        roles = TravelerInfo.objects.all()
        return render(request, 'sys_mgr/caidan.html', locals())

    def post(self, request):
        print(request.POST)
        id = request.POST.get('travel_id', None)  # 注意： form表单页面不建议使用id 字段名
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        id_card = request.POST.get('id_card')
        phone_num = request.POST.get('phone_num')
        go_date = request.POST.get('go_date')
        # 验证是否为空(建议:页面上验证是否为空)

        if id:
            # 更新
            role = TravelerInfo.objects.get(pk=id)
            role.name = name
            role.gender = gender
            role.id_card = id_card
            role.phone_num = phone_num
            role.go_date = go_date
            role.save()
        else:
           TravelerInfo.objects.create(name=name, gender=gender, id_card=id_card, phone_num=phone_num, go_date=go_date)

        return redirect('/caidan/')

    def delete(self, request):
        role_id = request.GET.get('id')
        role = TravelerInfo.objects.get(pk=role_id)
        role.delete()

        return JsonResponse({
            'status': 0,
            'msg': '删除成功!'
        })


class XttzView(View):
    def get(self, request):
        if request.GET.get('id', ''):
            role = SysInfo.objects.get(pk=request.GET.get('id'))
            return JsonResponse({
                'id': role.sys_info_id,
                'title': role.title,
                'info': role.info,
                'info_detail': role.info_detail
            })

        roles = SysInfo.objects.all()
        return render(request, 'sys_mgr/xttz.html', locals())

    def post(self, request):
        print(request.POST)
        id = request.POST.get('sys_info_id', None)  # 注意： form表单页面不建议使用id 字段名
        title = request.POST.get('title')
        info = request.POST.get('info')
        info_detail = request.POST.get('info_detail')
        # 验证是否为空(建议:页面上验证是否为空)

        if id:
            # 更新
            role = SysInfo.objects.get(pk=id)
            role.title = title
            role.info = info
            role.info_detail = info_detail
            role.save()
        else:
            SysInfo.objects.create(title=title, info=info, info_detail=info_detail)

        return redirect('/xttz/')

    def delete(self, request):
        role_id = request.GET.get('id')
        role = SysInfo.objects.get(pk=role_id)
        role.delete()

        return JsonResponse({
            'status': 0,
            'msg': '删除成功!'
        })


class QxglView(View):
    def get(self, request):
        if request.GET.get('id', ''):
            role = SysUser.objects.get(pk=request.GET.get('id'))
            return JsonResponse({
                'id': role.id,
                'name': role.name,
                'auth_string': role.auth_string,
                'email': role.email,
                'phone': role.phone
            })

        roles = SysUser.objects.all()
        return render(request, 'sys_mgr/qxgl.html', locals())

    def post(self, request):
        print(request.POST)
        id = request.POST.get('q_id', None)  # 注意： form表单页面不建议使用id 字段名
        name = request.POST.get('name')
        auth_string = request.POST.get('auth_string')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        # 验证是否为空(建议:页面上验证是否为空)

        if id:
            # 更新
            role = SysUser.objects.get(pk=id)
            role.name = name
            role.auth_string = auth_string
            role.email = email
            role.phone = email
            role.save()
        else:
            SysUser.objects.create(name=name, auth_string=auth_string)

        return redirect('/qxgl/')

    def delete(self, request):
        role_id = request.GET.get('id')
        role = SysUser.objects.get(pk=role_id)
        role.delete()

        return JsonResponse({
            'status': 0,
            'msg': '删除成功!'
        })