from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from myadmin.models import *
from utils.owner import owner_page


class InfoView(View):
    def get(self, request):
        if request.GET.get('id', ''):
            role = Views.objects.get(pk=request.GET.get('id'))
            return JsonResponse({
                'id': role.v_id,
                'name': role.name,
                'price': role.price,
                'v_desc': role.v_desc,
                'v_pic': role.v_pic,
                'travel_way': role.travel_way,
                'diamonds': role.diamonds
            })

        roles = Views.objects.all()
        id = request.session.get('id')
        # views = Views.objects.all()
        roles1, allPage, curPage, count = owner_page(request, roles)

        return render(request, 'jingdian_mgr/jingdian.html', locals())

    # def get_all_goods(self, request):
    #
    #     return render(request, "jingdian_mgr/jingdian.html", locals())

    def post(self, request):
        print(request.POST)
        id = request.POST.get('v_id', None)  # 注意： form表单页面不建议使用id 字段名
        name = request.POST.get('name')
        price = request.POST.get('price')
        v_desc = request.POST.get('v_desc')
        v_pic = request.POST.get('v_pic')
        travel_way = request.POST.get('travel_way')
        diamonds = request.POST.get('diamonds')
        # 验证是否为空(建议:页面上验证是否为空)

        if id:
            # 更新
            role = Views.objects.get(pk=id)
            role.name = name
            role.code = price
            role.v_desc = v_desc
            role.v_pic = v_pic
            role.travel_way = travel_way
            role.diamonds = diamonds
            role.save()
        else:
            Views.objects.create(name=name, price=price, v_desc=v_desc, v_pic=v_pic, travel_way=travel_way, diamonds=diamonds)

        return redirect('/info/')

    def delete(self, request):
        role_id = request.GET.get('id')
        # print(role_id)
        role = Views.objects.get(pk=role_id)
        role.delete()

        return JsonResponse({
            'status': 0,
            'msg': '删除成功!'
        })




class PlView(View):
    def get(self, request):
        return render(request, 'jingdian_mgr/pinglun.html')


# class TjView(View):
#     def get(self, request):
#         return render(request, 'jingdian_mgr/tuijian.html')
#
#
# class ZsfjView(View):
#     def get(self, request):
#         return render(request, 'jingdian_mgr/zsfj.html')