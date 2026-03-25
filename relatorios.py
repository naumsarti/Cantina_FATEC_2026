from controle_estoque import Estoque
from controle_pagamento import HistoricoPagamentos
from controle_consumo import GerenciadorConsumo

class RelatorioService:
    def gerar_relatorio_vendas(self, estoque: Estoque):
        print(f"\n{'='*20} ESTOQUE ATUAL {'='*20}")
        atual = estoque.head
        if not atual: print("Estoque vazio.")
        
        while atual:
            print(f"• {atual.nome} | Preço: R${atual.preco_venda:.2f} | Qtd: {atual.quantidade}")
            atual = atual.proximo

    def gerar_relatorio_consumo(self, consumo: GerenciadorConsumo, pagamentos: HistoricoPagamentos):
        print(f"\n{'='*15} RESUMO DE CONSUMO E CAIXA {'='*15}")
        
        item = consumo.head
        while item:
            print(f"- {item.pagador} consumiu {item.produto_nome} (Total: R${item.valor_total:.2f})")
            item = item.proximo

        pg = pagamentos.head
        total_caixa = 0
        while pg:
            print(f"- PGTO: {pg.pagador} ({pg.curso}) | R${pg.valor:.2f}")
            total_caixa += pg.valor
            pg = pg.proximo
        print(f"SALDO TOTAL EM CAIXA: R${total_caixa:.2f}")