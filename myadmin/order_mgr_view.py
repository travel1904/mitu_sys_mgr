from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from myadmin.models import *
from utils.owner import owner_page


class JifenView(View):
    def get(self, request):
        if request.GET.get('id', ''):
            role = ScoreSave.objects.get(pk=request.GET.get('id'))
            return JsonResponse({
                'id': role.score_save_id,
                # 'ud_id': role.ud_id,
                'num': role.num,
                'record': role.get_record,
                'time': role.get_time,
                'way': role.get_way
            })

        roles = ScoreSave.objects.all()
        return render(request, 'order_mgr/jifen.html', locals())

    def post(self, request):
        print(request.POST)
        id = request.POST.get('score_save_id', None)  # 注意： form表单页面不建议使用id 字段名
        # ud_id = request.POST.get('ud_id')
        num = request.POST.get('num')
        get_record = request.POST.get('get_record')
        get_time = request.POST.get('get_time')
        get_way = request.POST.get('get_way')
        # 验证是否为空(建议:页面上验证是否为空)

        if id:
            # 更新
            role = ScoreSave.objects.get(pk=id)
            # role.ud_id = ud_id
            role.num = num  # 建议不修改code
            role.get_record = get_record
            role.get_time = get_time
            role.get_way = get_way
            role.save()
        else:
           ScoreSave.objects.create(num=num, get_record=get_record, get_time=get_time, get_way=get_way)

        return redirect('/jifen/')

    def delete(self, request):
        role_id = request.GET.get('id')
        role = ScoreSave.objects.get(pk=role_id)
        role.delete()

        return JsonResponse({
            'status': 0,
            'msg': '删除成功!'
        })


class YhquanView(View):
    def get(self, request):
        if request.GET.get('id', ''):
            role = SysTicket.objects.get(pk=request.GET.get('id'))
            return JsonResponse({
                'id': role.sys_ticket_id,
                # 'ud_id': role.ud_id,
                'name': role.st_name,
                'account': role.st_money,
                'desc': role.st_ticket_desc,
                'use': role.is_use,
                'time': role.create_time
            })

        roles = SysTicket.objects.all()
        return render(request, 'order_mgr/yhquan.html', locals())

    def post(self, request):
        print(request.POST)
        id = request.POST.get('ticket_id', None)  # 注意： form表单页面不建议使用id 字段名
        # ud_id = request.POST.get('ud_id')
        st_name = request.POST.get('st_name')
        st_money = request.POST.get('st_money')
        st_ticket_desc = request.POST.get('st_ticket_desc')
        is_use = request.POST.get('is_use')
        create_time = request.POST.get('create_time')
        # 验证是否为空(建议:页面上验证是否为空)

        if id:
            # 更新
            role = SysTicket.objects.get(pk=id)
            # role.ud_id = ud_id
            role.st_name = st_name
            role.st_money = st_money
            role.st_ticket_desc = st_ticket_desc
            role.is_use = is_use
            role.create_time = create_time
            role.save()
        else:
            SysTicket.objects.create(st_name=st_name, st_money=st_money, st_ticket_desc=st_ticket_desc, is_use=is_use, create_time=create_time)

        return redirect('/yhquan/')

    def delete(self, request):
        role_id = request.GET.get('id')
        role = SysTicket.objects.get(pk=role_id)
        role.delete()

        return JsonResponse({
            'status': 0,
            'msg': '删除成功!'
        })


class OrderInfoiew(View):
    def get(self, request):
        if request.GET.get('id', ''):
            role = OrderTable.objects.get(pk=request.GET.get('id'))
            return JsonResponse({
                'id': role.order_id,
                'get_time': role.get_time,
                'pay_time': role.pay_time,
                'last_time': role.last_time,
                'status': role.status,
                'no_need': role.no_need,
                'return_money_time': role.is_talk
            })

        roles = OrderTable.objects.all()
        id = request.session.get('id')
        # views = Views.objects.all()
        roles1, allPage, curPage, count = owner_page(request, roles)
        return render(request, 'order_mgr/order_info.html', locals())

    def post(self, request):
        print(request.POST)
        id = request.POST.get('ticket_id', None)  # 注意： form表单页面不建议使用id 字段名
        get_time = request.POST.get('get_time')
        pay_time = request.POST.get('pay_time')
        last_time = request.POST.get('last_time')
        status = request.POST.get('status')
        no_need = request.POST.get('no_need')
        return_money_time = request.POST.get('return_money_time')
        is_talk = request.POST.get('is_talk')
        # 验证是否为空(建议:页面上验证是否为空)

        if id:
            # 更新
            role = OrderTable.objects.get(pk=id)
            role.get_time = get_time
            role.pay_time = pay_time
            role.last_time = last_time
            role.status = status
            role.no_need = no_need
            role.return_money_time = return_money_time
            role.is_talk = is_talk
            role.save()
        else:
            OrderTable.objects.create(get_time=get_time, pay_time=pay_time, last_time=last_time, status=status, no_need=no_need, return_money_time=return_money_time, is_talk=is_talk)

        return redirect('/order_count/')

    def delete(self, request):
        role_id = request.GET.get('id')
        role = OrderTable.objects.get(pk=role_id)
        role.delete()

        return JsonResponse({
            'status': 0,
            'msg': '删除成功!'
        })
