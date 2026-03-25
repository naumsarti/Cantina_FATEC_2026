import datetime

class Pagamento:
    def __init__(self, pagador, categoria, curso, valor):
        self._pagador = pagador
        self._categoria = categoria
        self._curso = curso
        self._valor = valor
        self._data_hora = datetime.datetime.now()
        self.proximo = None


    @property
    def pagador(self): return self._pagador
    @property
    def categoria(self): return self._categoria
    @property
    def curso(self): return self._curso
    @property
    def valor(self): return self._valor
    @property
    def data_hora(self): return self._data_hora

class HistoricoPagamentos:
    def __init__(self):
        self.head = None

    def registrar_pagamento(self, pagamento):
        if not self.head:
            self.head = pagamento
        else:
            atual = self.head
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = pagamento
        print(f"Pagamento de R${pagamento.valor:.2f} registrado para {pagamento.pagador}.")