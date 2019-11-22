from django.shortcuts import render
from django.views import View


class UserCountView(View):
	def get(self, request):
		return render(request, 'info_count/user_count.html')
	
	def post(self, request):
		pass
	
	def delete(self, request):
		pass
	
	def put(self, request):
		pass


class DingdCountiew(View):
	def get(self, request):
		return render(request, 'info_count/jingd_count.html')
	
	def post(self, request):
		pass
	
	def delete(self, request):
		pass
	
	def put(self, request):
		pass


class OrderView(View):
	def get(self, request):
		return render(request, 'info_count/order_count.html')
	
	def post(self, request):
		pass
	
	def delete(self, request):
		pass
	
	def put(self, request):
		pass
