from django.shortcuts import render
from django.views import View


class RoleView(View):
	def get(self, request):
		return render(request, 'sys_mgr/role.html')
	
	def post(self, request):
		pass
	
	def delete(self, request):
		pass
	
	def put(self, request):
		pass
	
	
class UserView(View):
	def get(self,request):
		return render(request, 'sys_mgr/user.html')
	
	def post(self, request):
		pass
	
	def delete(self, request):
		pass
	
	def put(self, request):
		pass


class AuthorityView(View):
	def get(self, request):
		return render(request, 'sys_mgr/authority.html')
	
	def post(self, request):
		pass
	
	def delete(self, request):
		pass
	
	def put(self, request):
		pass


class CaidanView(View):
	def get(self, request):
		return render(request, 'sys_mgr/caidan.html')
	
	def post(self, request):
		pass
	
	def delete(self, request):
		pass
	
	def put(self, request):
		pass