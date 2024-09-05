# coding: utf-8
import logging

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .service import produtos_svc

logger = logging.getLogger(__name__)


@csrf_exempt
def listar_estoque_produto(request):
    """Adiciona Produto"""
    logger.info("API add new produto.")
    listar_estoque = produtos_svc.listar_estoque_produtos()
    return JsonResponse({"produtos": listar_estoque})


@require_http_methods(["POST"])
def salvar_pedido(request):
    """Salvar pedido de entrega"""
    logger.info("TODO")
    return JsonResponse({"pedido": None}, status=201)
