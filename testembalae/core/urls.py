from django.urls import path

from . import views

urlpatterns = [
    path("estoque/produtos", views.listar_estoque_produto),
    path("pedidos/salvar", views.salvar_pedido),
]
