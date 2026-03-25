class Consumo:
    def __init__(self, pagador, produto_nome, quantidade, valor_total):
        self._pagador = pagador
        self._produto_nome = produto_nome
        self._quantidade = quantidade
        self._valor_total = valor_total
        self.proximo = None


    @property
    def pagador(self): return self._pagador
    @property
    def produto_nome(self): return self._produto_nome
    @property
    def quantidade(self): return self._quantidade
    @property
    def valor_total(self): return self._valor_total

class GerenciadorConsumo:
    def __init__(self):
        self.head = None

    def registrar_consumo(self, pagador, produto_nome, quantidade, valor_unitario):
        novo_consumo = Consumo(pagador, produto_nome, quantidade, (quantidade * valor_unitario))
        if not self.head:
            self.head = novo_consumo
        else:
            atual = self.head
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_consumo
        return novo_consumo