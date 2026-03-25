import datetime

class Produto:
    def __init__(self, nome, preco_compra, preco_venda, data_vencimento, quantidade):
        self._nome = nome
        self._preco_compra = preco_compra
        self._preco_venda = preco_venda
        self._data_vencimento = data_vencimento 
        self._data_compra = datetime.datetime.now()
        self._quantidade = quantidade
        self.proximo = None  


    @property
    def nome(self): return self._nome
    @property
    def preco_compra(self): return self._preco_compra
    @property
    def preco_venda(self): return self._preco_venda
    @property
    def data_vencimento(self): return self._data_vencimento
    @property
    def quantidade(self): return self._quantidade

    @quantidade.setter
    def quantidade(self, valor):
        if valor >= 0:
            self._quantidade = valor
        else:
            print("Erro: Quantidade não pode ser negativa.")

    def __str__(self):
        return f"{self._nome} | Qtd: {self._quantidade} | Vence: {self._data_vencimento}"

class Estoque:
    def __init__(self):
        self.head = None

    def adicionar_produto(self, produto):
        if not self.head:
            self.head = produto
        else:
            atual = self.head
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = produto

    def vender_item(self, nome_produto, quantidade_venda):
        atual = self.head
        while atual:
            if atual.nome == nome_produto and atual.quantidade > 0:
                if atual.quantidade >= quantidade_venda:
                    atual.quantidade -= quantidade_venda
                    return True
            atual = atual.proximo
        return False