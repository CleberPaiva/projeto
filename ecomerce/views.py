from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, login
from .models import Produto, EmailContato
from .form import ProdutoCadastro, FormEmail
from django.contrib import messages
from django.contrib.auth.models import Group, User, Permission
from cart.forms import CartAddProductForm
from orders.models import Order
from orders.models import Item
from orders.models import Validar
from django.core.mail import EmailMessage

from django.core.mail import send_mail

@login_required(login_url='/loginadm/')
def adm_produto(request):
    data = {}
    data['produtos'] = Produto.objects.all()
    return render(request, 'admproduto.html', data)

#produto
def produto_view(request):
    if request.POST:
        form = ProdutoCadastro(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('url_admproduto')
    else:
        form = ProdutoCadastro()
    return render(request, "produto.html",{'form': form})


def update(request, id):
    data ={}
    produto = Produto.objects.get(id=id)
    
    form = ProdutoCadastro(instance=produto)
    if (request.method) == 'POST':
        form = ProdutoCadastro(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('url_admproduto')
    data['form'] = form
    data['produto'] = produto
    return render(request, "produto.html", data)

def delete(request, id):
    produto = Produto.objects.get(id=id)
    produto.delete()
    return redirect('url_adm')
#fim produto

#pagina de compras
@login_required(login_url='/login/')
def pag_compras(request):
    data = {}
    data['produtos'] = Produto.objects.all()
    data["form"] = CartAddProductForm()
    return render(request, 'compras.html', data,)

#adm geral
@login_required(login_url='/loginadm/')
def adm_geral(request):
    if request.user:
        uso = request.user.groups.all()
        if str(uso[0]) == 'Comprador':
            return redirect('url_login_adm')
    return render(request, 'adm.html')

#adm pedido
@login_required(login_url='/loginadm/')
def adm_pedido(request):
    data = {}
    dados = []
    pedidos = Order.objects.all()
    pedidos_val = Validar.objects.all()
    for x in pedidos_val:
        dados.append(x.id)
    data['pedidos']  = pedidos
    data['items']  =  Item.objects.all()
    data['dados'] = dados
    return render(request, 'admpedido.html', data)

def valid_pedido(request, num_id, motivo):
    if  not Validar.objects.filter(id=num_id) and motivo == 'recusar':
        pedido_val = Validar.objects.create(num_id=num_id, motivo=motivo)
    return redirect('admpedido')

#adm galeria
@login_required(login_url='/loginadm/')
def adm_galeria(request):

    return render(request, 'admgaleria.html')


def pag_index(request):
    return render(request, 'index.html')

#contatos
def contatos(request):
    return render(request, 'contato.html')

def login_user(request):
    return render(request, 'login.html')

def login_submit(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            print(usuario.get_all_permissions())
            return redirect('url_compras')
        else:
            messages.error(request, 'Email ou senha inválidos')
    
    return redirect('/login/')

def logout_user(request):
    logout(request)
    return redirect('url_index')


def admlogin_user(request):
    return render(request, 'loginadm.html')

def admlogin_submit(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            uso = request.user.groups.all()
            print(usuario.get_all_permissions())
            if str(uso[0]) == 'Administrador':
                return redirect('url_adm')
        else:
            messages.error(request, 'Usuário ou senha inválidos')
    return redirect('/loginadm/')

def admlogout_user(request):
    logout(request)
    return redirect('url_index')


def cadastrar(request):
    return render(request, 'cadastrar.html')

def cadastrar_submit(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    
    novoUsusario = User.objects.create_user(username=username, email=email, password=password,)
    mygroup = Group.objects.get(name='Comprador')
    novoUsusario.groups.add(mygroup)
    novoUsusario.is_staff = False
    novoUsusario.save()
    return redirect('url_compras')

