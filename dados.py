import pickle
import random
from faker import Faker
from estoque import Produto, Estoque

class GeradorDados:
    """Classe responsável por gerar dados aleatórios para popular o sistema."""
    
    def __init__(self):
        self.fake = Faker()
        self.produtos_base = ["Coca-Cola", "Pepsi", "Guaraná Antarctica", "Salgadinho Torcida", "Coxinha", "Pão de Queijo", "Suco Del Valle", "Chocolate Bis"]

    def gerar_estoque_aleatorio(self, quantidade_lotes=10):
        """Gera uma estrutura de estoque populada aleatoriamente."""
        novo_estoque = Estoque()
        
        for _ in range(quantidade_lotes):
            nome = random.choice(self.produtos_base)
            preco_compra = round(random.uniform(1.0, 5.0), 2)
            # Preço de venda geralmente maior que o de compra
            preco_venda = round(preco_compra * random.uniform(1.3, 2.0), 2)
            
            # Gera data de vencimento futura (entre 10 e 100 dias)
            data_vencimento = self.fake.future_date(end_date='+100d').strftime("%d/%m/%Y")
            quantidade = random.randint(5, 20)
            
            produto = Produto(nome, preco_compra, preco_venda, data_vencimento, quantidade)
            novo_estoque.adicionar_produto(produto)
            
        return novo_estoque

class SalvarDados:
    """Classe para salvar dados de maneira não volátil usando pickle."""

    @staticmethod
    def salvar_estoque(estoque, nome_arquivo="estoque.pkl"):
        """Armazena o objeto estoque em um arquivo binário."""
        try:
            with open(nome_arquivo, 'wb') as f:
                pickle.dump(estoque, f)
            print(f"Dados salvos com sucesso em {nome_arquivo}.")
        except Exception as e:
            print(f"Erro ao salvar dados: {e}")

class CarregarDados:
    """Classe para carregar dados."""

    @staticmethod
    def carregar_estoque(nome_arquivo="estoque.pkl"):
        """Carrega o objeto estoque do arquivo binário."""
        try:
            with open(nome_arquivo, 'rb') as f:
                estoque = pickle.load(f)
            print(f"Dados carregados com sucesso de {nome_arquivo}.")
            return estoque
        except FileNotFoundError:
            print("Arquivo de dados não encontrado. Iniciando novo estoque.")
            return Estoque()
        except Exception as e:
            print(f"Erro ao carregar: {e}")
            return Estoque()

# Exemplo de uso para teste
if __name__ == "__main__":
    # Gerando dados novos
    gerador = GeradorDados()
    estoque_novo = gerador.gerar_estoque_aleatorio()
    
    # Usando a classe de salvamento
    SalvarDados.salvar_estoque(estoque_novo)
    
    # Usando a classe de carregamento
    estoque_recuperado = CarregarDados.carregar_estoque()