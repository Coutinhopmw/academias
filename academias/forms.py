from django import forms
from .models import Usuarios
from django.contrib.auth.forms import UserCreationForm         

class SignupForm(UserCreationForm):
    nome = forms.CharField(label='Nome Completo', max_length=255)
    cpf = forms.CharField(label='CPF', max_length=14, widget=forms.TextInput(attrs={'placeholder': '000.000.000-00'}))
    nascimento = forms.CharField(label="Data nascimento", widget=forms.TextInput(attrs={'placeholder':'DD/MM/AAAA'}))
    telefone = forms.CharField(label='Telefone', max_length=15,widget=forms.TextInput(attrs={'placeholder':'(00)00000-0000'}))
    endereco = forms.CharField(label='Endereço', max_length=255)

    planos = [
        ('BASICO', 'BASICO'),
        ('PREMIUM', 'PREMIUM'),
        ('VIP', 'VIP'),
    ]

    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Senha', widget=forms.PasswordInput)

    class Meta:
        model = Usuarios
        fields = ['email', 'password1', 'password2','nascimento', 'cpf', 'telefone', 'nome']

    #  class Meta:
        # model = Usuarios
        # fields = ['email', 'password1', 'password2','nascimento', 'cpf', 'telefone', 'nome', 'mestre', 'professor', 'cargo', 'graduacao','foto_perfil']

    # Removendo a obrigatoriedade do campo 'username'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('username', None)