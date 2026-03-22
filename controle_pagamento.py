import datetime

class Pagamento:
    def __init__(self, pagador, categoria, curso, valor):
        self.pagador = pagador
        self.categoria = categoria  # Aluno, Servidor ou Professor
        self.curso = curso          # IA ou ESG
        self.valor = valor
        self.data_hora = datetime.datetime.now()
        self.proximo = None

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
        print(f"Pagamento de R${pagamento.valor} por {pagamento.pagador} registrado via PIX.")
