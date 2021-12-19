"""projeto_ope URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from django.urls import include

from ecomerce.views import produto_view, adm_produto, update, delete, pag_compras, adm_geral, adm_pedido,adm_galeria,pag_index, contatos,login_user,login_submit, logout_user,admlogin_user, admlogin_submit,  admlogout_user, cadastrar, cadastrar_submit, valid_pedido


urlpatterns = [
    path('admin/', admin.site.urls),
    path('produto/', produto_view, name="url_produto"),
    path('admproduto/', adm_produto, name="url_admproduto"),
    path('admpedido/', adm_pedido, name="admpedido"),
    path('admgaleria/', adm_galeria, name="url_admgaleria"),
    path('update/<int:id>', update, name="url_update"),
    path('delete/<int:id>', delete, name="url_delete"),
    path('adm/', adm_geral, name="url_adm"),
    path('compras/', pag_compras, name="url_compras"),
    path('', pag_index, name="url_index"),
    path('contato/', contatos, name="url_contato"),
    path('login/', login_user, name="url_login"),
    path('login/submit', login_submit, name="url_submit_login"),
    path('logout/', logout_user, name="url_logout"),
    path('loginadm/', admlogin_user, name="url_login_adm"),
    path('loginadm/submit', admlogin_submit, name="url_submit_login"),
    path('logoutadm/', admlogout_user, name="url_logout"),
    path('cadastrar/', cadastrar, name="url_cadastrar"),
    path('cadastrar/submit', cadastrar_submit, name="url_cadastrar_submit"),
    path('cart/', include("cart.urls"), name="cart"),
    path("orders/", include("orders.urls")),
    path('admpedido/<int:num_id>/<str:motivo>/', valid_pedido, name="url_validar"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
