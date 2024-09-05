from django.db import models


class Fornecedor(models.Model):
    """
    Descrição: Fornecedor, Gráfica
    """

    nome = models.CharField(max_length=256, unique=True)
    cnpj = models.CharField(max_length=64, null=True, blank=True, unique=True)
    valor_pedido_minimo = models.IntegerField(default=0)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ("nome",)


class Produto(models.Model):
    fornecedor = models.ForeignKey(
        Fornecedor, null=True, blank=True, on_delete=models.CASCADE
    )
    nome = models.CharField(max_length=128, default="")
    unidade = models.CharField(max_length=16, default="UN")
    quantidade_minima = models.IntegerField(default=0)
    descricao = models.TextField(max_length=512, null=True, blank=True)
    imagem = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return f"{self.nome} [{self.fornecedor}]"

    def to_dict_json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "unidade": self.unidade,
            "quantidade_minima": self.quantidade_minima,
            "descricao": self.descricao,
            "imagem": self.imagem,
        }


class ProdutoEstoque(models.Model):
    """ """

    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    valor_unitario = models.DecimalField(
        decimal_places=5, max_digits=10, default=0.00000
    )
    lote = models.CharField(max_length=32, default="")
    quantidade_disponivel = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.produto}: {self.quantidade_disponivel}"

    def to_dict_json(self):
        return {
            "id": self.id,
            "produto": self.produto.to_dict_json(),
            "lote": self.lote,
            "quantidade_disponivel": self.quantidade_disponivel,
        }


class PedidoEntrega(models.Model):
    """
    Descrição: entidade que traz os eventos de compra do estoque
    """

    criado_em = models.DateTimeField(null=True, blank=True, auto_now_add=True)

    def __str__(self):
        return {self.pk}


class PedidoEntregaItem(models.Model):
    """
    Descrição: tabela de evento das compras fracionarias
    por um estabelecimento a nível produto.id
    """

    pedido_entrega = models.ForeignKey(PedidoEntrega, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=0)
    valor_unitario = models.DecimalField(
        null=True, blank=True, decimal_places=5, max_digits=10
    )
    data_entrega_prevista = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Entrega Item: {self.pk}"
