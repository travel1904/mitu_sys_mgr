from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from myadmin.models import *
from utils.owner import owner_page


class WzglView(View):
    def get(self, request):
        if request.GET.get('id', ''):
            role = Article.objects.get(pk=request.GET.get('id'))
            return JsonResponse({
                'id': role.article_id,
                # 'ud_id': role.ud_id,
                'title': role.a_title,
                'image': role.a_image,
                'num': role.view_num,
                'time': role.create_time
            })

        roles = Article.objects.all()
        id = request.session.get('id')
        # views = Views.objects.all()
        roles1, allPage, curPage, count = owner_page(request, roles)
        return render(request, 'wenzh_mgr/wzgl.html', locals())

    def post(self, request):
        print(request.POST)
        id = request.POST.get('article_id', None)  # 注意： form表单页面不建议使用id 字段名
        # ud_id = request.POST.get('ud_id')
        a_title = request.POST.get('a_title')
        a_image = request.POST.get('a_image')
        view_num = request.POST.get('view_num')
        create_time = request.POST.get('create_time')
        # 验证是否为空(建议:页面上验证是否为空)

        if id:
            # 更新
            role = Article.objects.get(pk=id)
            # role.ud_id = ud_id
            role.a_title = a_title
            role.a_image = a_image
            role.view_num = view_num
            role.create_time = create_time
            role.save()
        else:
            Article.objects.create(a_title=a_title, a_image=a_image, view_num=view_num, create_time=create_time)

        return redirect('/wzgl/')

    def delete(self, request):
        role_id = request.GET.get('id')
        role = Article.objects.get(pk=role_id)
        role.delete()

        return JsonResponse({
            'status': 0,
            'msg': '删除成功!'
        })


class LunbtView(View):
    def get(self, request):
        if request.GET.get('id', ''):
            role = WheelTable.objects.get(pk=request.GET.get('id'))
            return JsonResponse({
                'id': role.wheel_id,
                # 'ud_id': role.ud_id,
                'img_url': role.img_url,
            })

        roles = WheelTable.objects.all()
        return render(request, 'wenzh_mgr/lunbt.html', locals())

    def post(self, request):
        print(request.POST)
        id = request.POST.get('wheel_id', None)  # 注意： form表单页面不建议使用id 字段名
        # ud_id = request.POST.get('ud_id')
        img_url = request.POST.get('img_url')
        # 验证是否为空(建议:页面上验证是否为空)

        if id:
            # 更新
            role = WheelTable.objects.get(pk=id)
            # role.ud_id = ud_id
            role.img_url = img_url
            role.save()
        else:
            WheelTable.objects.create(img_url=img_url)

        return redirect('/lunbt/')

    def delete(self, request):
        role_id = request.GET.get('id')
        role = WheelTable.objects.get(pk=role_id)
        role.delete()

        return JsonResponse({
            'status': 0,
            'msg': '删除成功!'
        })


class WzplView(View):
    def get(self, request):
        if request.GET.get('id', ''):
            role = Article.objects.get(pk=request.GET.get('id'))
            return JsonResponse({
                'id': role.article_id,
                # 'ud_id': role.ud_id,
                'title': role.a_title,
                'talk': role.a_talk,
            })

        roles = Article.objects.all()
        return render(request, 'wenzh_mgr/wzpl.html', locals())

    def post(self, request):
        print(request.POST)
        id = request.POST.get('article_id', None)  # 注意： form表单页面不建议使用id 字段名
        # ud_id = request.POST.get('ud_id')
        a_title = request.POST.get('a_title')
        a_talk = request.POST.get('a_talk')
        # 验证是否为空(建议:页面上验证是否为空)

        if id:
            # 更新
            role = Article.objects.get(pk=id)
            # role.ud_id = ud_id
            role.a_title = a_title
            role.a_talk = a_talk
            role.save()
        else:
            Article.objects.create(a_title=a_title, a_talk=a_talk)

        return redirect('/wzpl/')

    def delete(self, request):
        role_id = request.GET.get('id')
        role = Article.objects.get(pk=role_id)
        role.delete()

        return JsonResponse({
            'status': 0,
            'msg': '删除成功!'
        })