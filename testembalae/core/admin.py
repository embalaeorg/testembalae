from django.contrib import admin

from .models import Fornecedor, Produto, ProdutoEstoque


admin.site.register(Fornecedor)
admin.site.register(Produto)
admin.site.register(ProdutoEstoque)
