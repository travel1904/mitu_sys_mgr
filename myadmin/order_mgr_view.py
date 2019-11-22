from django.shortcuts import render
from django.views import View


class JifenView(View):
	def get(self, request):
		return render(request, 'order_mgr/jifen.html')
	
	def post(self, request):
		pass
	
	def delete(self, request):
		pass
	
	def put(self, request):
		pass


class YhquanView(View):
	def get(self, request):
		return render(request, 'order_mgr/yhquan.html')
	
	def post(self, request):
		pass
	
	def delete(self, request):
		pass
	
	def put(self, request):
		pass


class OrderInfoiew(View):
	def get(self, request):
		return render(request, 'order_mgr/order_info.html')
	
	def post(self, request):
		pass
	
	def delete(self, request):
		pass
	
	def put(self, request):
		pass