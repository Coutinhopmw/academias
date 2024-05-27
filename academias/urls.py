from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from academias.views import Index,Loja,Login,Horarios,CadastroUsuario

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name ='index'), 
    path('loja/', Loja.as_view(), name='loja'),
    path('login/', Login.as_view(), name='login'),
    path('horarios/', Horarios.as_view(), name='horarios'),
    path('cadastro-usuario/', CadastroUsuario.as_view(), name='CadastroUsuario'),
]
