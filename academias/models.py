from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser,Group, Permission
from django.db import models


class Usuarios(AbstractUser):
    groups = models.ManyToManyField(Group, verbose_name='groups', blank=True, related_name='usuarios_set')
    user_permissions = models.ManyToManyField(Permission, verbose_name='user permissions', blank=True, related_name='usuarios_set')
    nome = models.CharField(max_length=255)
    nascimento = models.CharField(max_length=11)
    cpf = models.CharField(max_length=14, unique=True)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=16)
    email = models.EmailField(max_length=254, unique=True)
    data_inscricao = models.DateTimeField(auto_now_add=True)
    data_desligamento = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome', 'cpf', 'nascimento', 'telefone']
    # REQUIRED_FIELDS = ['nome', 'cpf', 'nascimento', 'telefone', 'mestre', 'professor','graduacao','cargo']

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.nome
        super().save(*args, **kwargs)
    
    class Meta:
        db_table = 'usuarios'

class Produtos(models.Model):
    Nome = models.CharField(max_length=255)
    codigo = models.CharField(max_length=255)
    capa = models.ImageField(upload_to='capa/', null=True, blank=True)
    descricao =  models.CharField(max_length=255)
    valor = models.FloatField(max_length=4)
    quantidade_vendas = models.IntegerField(max_length=20)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'Produtos'
