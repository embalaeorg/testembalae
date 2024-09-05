import logging

from ..models import ProdutoEstoque

logger = logging.getLogger(__name__)


def listar_estoque_produtos() -> list:
    logger.info("SERVICE listar produto")
    produtos = ProdutoEstoque.objects.filter(quantidade_disponivel__gt=0)
    return [item.to_dict_json() for item in produtos]
