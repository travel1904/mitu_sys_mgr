from django.shortcuts import render
from django.views import View


class InfoView(View):
	def get(self, request):
		return render(request, 'jdian_mgr/jingdian.html')
	
	def post(self, request):
		pass
	
	def delete(self, request):
		pass
	
	def put(self, request):
		pass


class PlView(View):
	def get(self, request):
		return render(request, 'jdian_mgr/jingdian.html')
	
	def post(self, request):
		pass
	
	def delete(self, request):
		pass
	
	def put(self, request):
		pass


class TjView(View):
	def get(self, request):
		return render(request, 'jdian_mgr/tuijian.html')
	
	def post(self, request):
		pass
	
	def delete(self, request):
		pass
	
	def put(self, request):
		pass


class ZsfjView(View):
	def get(self, request):
		return render(request, 'jdian_mgr/zsfj.html')
	
	def post(self, request):
		pass
	
	def delete(self, request):
		pass
	
	def put(self, request):
		pass