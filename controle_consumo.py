class Consumo:
    def __init__(self, pagador, produto_nome, quantidade, valor_total):
        self.pagador = pagador
        self.produto_nome = produto_nome
        self.quantidade = quantidade
        self.valor_total = valor_total
        self.proximo = None

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