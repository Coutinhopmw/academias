from django.contrib.auth.mixins import LoginRequiredMixin
from academias.models import Usuarios
from .forms import  SignupForm
from django.shortcuts import  get_object_or_404, redirect, render
from django.views.generic import View
from django.contrib.auth import authenticate, login
import logging

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


    # def post (self, request,*args, **kwargs):
    # form = SignupForm(request.POST,request.FILES)
    # if form.is_valid():
    #     form.save()
    #     return redirect('/login')
    # return render(request,self.template_name,{'form':form})

class CadastroUsuario(View):
    
    template_name = 'cadastro-usuario.html'

    def get(self, request):
        return render(request, 'cadastro-usuario.html')
    
    def post (self, request, *args, **kwargs):
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request,self.template_name,{'form':form})





