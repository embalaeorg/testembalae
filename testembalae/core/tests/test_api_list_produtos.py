import pytest
from unittest.mock import ANY

from testembalae.core.models import Produto, Fornecedor, ProdutoEstoque


@pytest.mark.django_db
def test_deve_retornar_lista_vazia(client, logged_jon):
    # Quando tentamos listar itens
    resp = client.get("/api/core/estoque/produtos")
    data = resp.json()

    # Entao recebemos um sem autorizacao
    assert resp.status_code == 200
    assert data.get("produtos") == []


@pytest.mark.django_db
def test_deve_listar_produto_em_estoque(client):
    # Dado um item criado
    grafica = Fornecedor.objects.create(nome="Gráfica")
    caixa = Produto.objects.create(
        fornecedor=grafica, nome="Caixa batata", unidade="UN"
    )
    ProdutoEstoque.objects.create(
        produto=caixa,
        valor_unitario=0.42,
        quantidade_disponivel=42,
    )

    # Quando listamos
    resp = client.get("/api/core/estoque/produtos")
    data = resp.json()

    # Entao
    assert resp.status_code == 200
    assert data == {
        "produtos": [
            {
                "id": ANY,
                "lote": "",
                "produto": {
                    "descricao": None,
                    "id": 1,
                    "imagem": None,
                    "nome": "Caixa batata",
                    "quantidade_minima": 0,
                    "unidade": "UN",
                },
                "quantidade_disponivel": 42,
            }
        ]
    }
