from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views import View


class UserCountView(View):
    def get(self, request):
        return render(request, 'tongji_count/user_count.html')


class OrderView(View):
    def get(self, request):
        return render(request, 'tongji_count/order_count.html')


class ScenicView(View):
    def get(self, request):
        return render(request, 'tongji_count/view_count.html')

