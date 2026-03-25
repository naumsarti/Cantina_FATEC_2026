import pickle
import random
from faker import Faker
from controle_estoque import Produto, Estoque

class GeradorDados:
    def __init__(self):
        self.fake = Faker()
        self.produtos_base = ["Coca-Cola", "Coxinha", "Suco Del Valle", "Chocolate Bis"]

    def gerar_estoque_aleatorio(self, quantidade_lotes=10):
        novo_estoque = Estoque()
        for _ in range(quantidade_lotes):
            nome = random.choice(self.produtos_base)
            p_compra = round(random.uniform(1.0, 5.0), 2)
            p_venda = round(p_compra * 1.5, 2)
            vencimento = self.fake.future_date(end_date='+100d').strftime("%d/%m/%Y")
            qtd = random.randint(5, 20)
            
            produto = Produto(nome, p_compra, p_venda, vencimento, qtd)
            novo_estoque.adicionar_produto(produto)
        return novo_estoque

class SalvarDados:
    @staticmethod
    def salvar_estoque(estoque, nome_arquivo="estoque.pkl"):
        with open(nome_arquivo, 'wb') as f:
            pickle.dump(estoque, f)

class CarregarDados:
    @staticmethod
    def carregar_estoque(nome_arquivo="estoque.pkl"):
        try:
            with open(nome_arquivo, 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            return Estoque()