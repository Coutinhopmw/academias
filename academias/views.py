from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class Index(View):
    def get (self,request):
        return render(request,'index.html')  

class Loja(View):
    def get(self, request):
        return render(request, 'loja.html')

class Login(View):
    def get(self, request):
        return render(request, 'login.html')

class Horarios(View):
    def get(self, request):
        return render(request, 'horarios.html')

class CadUser(View):
    def get(self, request):
        return render(request, 'cadUser.html')
