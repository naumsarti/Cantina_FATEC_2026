from controle_estoque import Estoque
from controle_pagamento import HistoricoPagamentos
from controle_consumo import GerenciadorConsumo

class RelatorioService:
    """Gera resumos formatados das atividades da Cantina."""

    def gerar_relatorio_vendas(self, estoque: Estoque):
        print(f"\n{'='*20} ESTOQUE ATUAL {'='*20}")
        
        atual, total_geral = estoque.head, 0
        if not atual:
            print("Estoque vazio.")
        
        while atual:
            print(f"• {atual}") # Usa o __str__ de Produto
            total_geral += atual.quantidade
            atual = atual.proximo
            
        print(f"{'-'*55}\nTotal de itens: {total_geral}\n{'='*55}")

    def gerar_relatorio_consumo(self, consumo: GerenciadorConsumo, pagamentos: HistoricoPagamentos):
        print(f"\n{'='*15} RESUMO DE CONSUMO E CAIXA {'='*15}")

        # Seção de Consumo
        print("\n[PRODUTOS CONSUMIDOS]")
        item = consumo.head
        if not item: print("Nenhum registro.")
        while item:
            print(f"- {item.pagador}: {item.quantidade}x {item.produto_nome} (R${item.valor_total:.2f})")
            item = item.proximo

        # Seção de Pagamentos
        print("\n[ENTRADAS PIX]")
        pg, total_caixa = pagamentos.head, 0
        if not pg: print("Nenhum pagamento.")
        while pg:
            data_pg = pg.data_hora.strftime('%d/%m/%Y %H:%M')
            print(f"- {pg.pagador} ({pg.categoria}): R${pg.valor:.2f} | {data_pg}")
            total_caixa += pg.valor
            pg = pg.proximo

        print(f"{'-'*55}\nSALDO TOTAL EM CAIXA: R${total_caixa:.2f}\n{'='*55}")