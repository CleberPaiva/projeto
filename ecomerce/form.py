from django import forms
from django.forms import ModelForm, fields
from .models import Produto, EmailContato
from django.forms.widgets import ClearableFileInput

class ProdutoCadastro(ModelForm):
    class Meta:
        model= Produto
        fields = ['nome', 'kg', 'sabor', 'preco', 'ativo', 'img']

class FormEmail(ModelForm):
    class Meta:
        model = EmailContato
        fields =['email', 'mensagem']