import datetime

# definição da classe produto para adicionar e remover
class Produto:
    def __init__(self, nome, preco_compra, preco_venda, data_vencimento, quantidade):
        self.nome = nome
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda
        self.data_vencimento = data_vencimento 
        self.data_compra = datetime.datetime.now()
        self.quantidade = quantidade
        self.proximo = None  

    def __str__(self):
        return f"{self.nome} | Qtd: {self.quantidade} | Vence: {self.data_vencimento}"


#     
class Estoque:
    def __init__(self):
        self.head = None  # Início da lista (item mais antigo)

    def adicionar_produto(self, produto):
        """Adiciona um produto ao final da lista (estoque novo)"""
        if not self.head:
            self.head = produto
        else:
            atual = self.head
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = produto
        print(f"Produto {produto.nome} adicionado ao estoque.")

    def vender_item(self, nome_produto, quantidade_venda):
        """Lógica de saída: remove do mais antigo para o mais novo"""
        atual = self.head
        while atual:
            if atual.nome == nome_produto and atual.quantidade > 0:
                if atual.quantidade >= quantidade_venda:
                    atual.quantidade -= quantidade_venda
                    print(f"Venda realizada! Restam {atual.quantidade} de {nome_produto}.")
                    return True
                else:
                    print("Quantidade insuficiente neste lote!")
                    return False
            atual = atual.proximo
        print("Produto não encontrado.")
        return False
    
