from django.shortcuts import render
from django.views import View


class JptjView(View):
	def get(self, request):
		return render(request, 'user_mgr/jptj.html')
	
	def post(self, request):
		pass
	
	def delete(self, request):
		pass
	
	def put(self, request):
		pass


class JyglView(View):
	def get(self, request):
		return render(request, 'user_mgr/jygl.html')
	
	def post(self, request):
		pass
	
	def delete(self, request):
		pass
	
	def put(self, request):
		pass


class WzglView(View):
	def get(self, request):
		return render(request, 'user_mgr/wzgl.html')
	
	def post(self, request):
		pass
	
	def delete(self, request):
		pass
	
	def put(self, request):
		pass


class WzplView(View):
	def get(self, request):
		return render(request, 'user_mgr/wzpl.html')
	
	def post(self, request):
		pass
	
	def delete(self, request):
		pass
	
	def put(self, request):
		pass