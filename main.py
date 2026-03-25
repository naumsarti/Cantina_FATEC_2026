import tkinter as tk
from tkinter import messagebox, ttk, scrolledtext
from datetime import datetime

from controle_estoque import Produto, Estoque
from controle_pagamento import Pagamento, HistoricoPagamentos
from controle_consumo import GerenciadorConsumo
from dados import GeradorDados, SalvarDados, CarregarDados

class CantinaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cantina - Gestão de Estoque e Vendas")
        self.root.geometry("800x600")
        
        self.estoque = Estoque()
        self.pagamentos = HistoricoPagamentos()
        self.consumo = GerenciadorConsumo()

        self.setup_ui()

    def setup_ui(self):
        self.tabs = ttk.Notebook(self.root)
        self.tabs.pack(expand=True, fill="both", padx=10, pady=10)

        self._criar_aba_vendas()
        self._criar_aba_estoque()
        self._criar_aba_relatorios()
        self._criar_aba_configuracoes()

    def _criar_aba_vendas(self):
        aba = ttk.Frame(self.tabs)
        self.tabs.add(aba, text="Realizar Venda")
        container = ttk.LabelFrame(aba, text="Formulário de Venda")
        container.pack(fill="x", padx=20, pady=20)

        # Campos de Venda
        ttk.Label(container, text="Produto em Estoque:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.combo_produto_venda = ttk.Combobox(container, state="readonly", width=30)
        self.combo_produto_venda.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(container, text="Quantidade:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.ent_venda_qtd = ttk.Entry(container)
        self.ent_venda_qtd.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(container, text="Nome do Pagador:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.ent_venda_pagador = ttk.Entry(container)
        self.ent_venda_pagador.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(container, text="Valor Total (R$):").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.ent_venda_valor = ttk.Entry(container)
        self.ent_venda_valor.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(container, text="Categoria:").grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.combo_cat = ttk.Combobox(container, values=["Aluno", "Professor", "Servidor"], state="readonly")
        self.combo_cat.grid(row=4, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(container, text="Curso:").grid(row=5, column=0, padx=5, pady=5, sticky="e")
        self.combo_curso = ttk.Combobox(container, values=["IA", "ESG"], state="readonly")
        self.combo_curso.grid(row=5, column=1, padx=5, pady=5, sticky="w")

        tk.Button(container, text="FINALIZAR VENDA", bg="#2ecc71", fg="white", 
                  font=("Arial", 10, "bold"), command=self.processar_venda).grid(row=6, column=0, columnspan=2, pady=20)

    def _criar_aba_estoque(self):
        aba = ttk.Frame(self.tabs)
        self.tabs.add(aba, text="Gestão de Estoque")
        form = ttk.LabelFrame(aba, text="Entrada Manual de Novo Lote")
        form.pack(fill="x", padx=20, pady=10)

        self.inputs_estoque = {}
        campos = [("Nome do Produto:", "e_nome"), ("Preço Compra (Unit):", "e_pcompra"), 
                  ("Preço Venda (Unit):", "e_pvenda"), ("Vencimento (DD/MM/AAAA):", "e_venc"), 
                  ("Quantidade:", "e_qtd")]
        
        for i, (label, var_name) in enumerate(campos):
            ttk.Label(form, text=label).grid(row=i, column=0, padx=5, pady=5, sticky="e")
            entry = ttk.Entry(form, width=30)
            entry.grid(row=i, column=1, padx=5, pady=5, sticky="w")
            self.inputs_estoque[var_name] = entry

        tk.Button(form, text="ADICIONAR AO ESTOQUE", bg="#3498db", fg="white", font=("Arial", 9, "bold"),
                  command=self.adicionar_estoque_manual).grid(row=6, column=0, columnspan=2, pady=15)

    def _criar_aba_relatorios(self):
        aba = ttk.Frame(self.tabs)
        self.tabs.add(aba, text="Relatórios")
        
        btn_frame = ttk.Frame(aba)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="GERAR RELATÓRIO", bg="#8e44ad", fg="white",
                  command=self.atualizar_visualizacao_relatorio).pack(side="left", padx=5)
        
        self.txt_area = scrolledtext.ScrolledText(aba, width=120, height=30, font=("Courier New", 10))
        self.txt_area.pack(padx=10, pady=10)

    def _criar_aba_configuracoes(self):
        aba = ttk.Frame(self.tabs)
        self.tabs.add(aba, text="Sistema")
        
        tk.Button(aba, text="CARREGAR DADOS DO DISCO", bg="#2980b9", fg="white", width=40,
                  command=self.carregar_dados_sistema).pack(pady=20)
        
        tk.Button(aba, text="SALVAR ESTADO ATUAL", bg="#27ae60", fg="white", width=40,
                  command=self.salvar_dados_sistema).pack(pady=10)

        tk.Button(aba, text="GERAR DADOS DE TESTE (FAKER)", bg="#e67e22", fg="white", width=40,
                  command=self.gerar_faker_seguro).pack(pady=40)


    def _atualizar_lista_produtos_venda(self):
        nomes = []
        atual = self.estoque.head
        while atual:
            if atual.nome not in nomes and atual.quantidade > 0:
                nomes.append(atual.nome)
            atual = atual.proximo
        self.combo_produto_venda['values'] = nomes

    def adicionar_estoque_manual(self):
        try:
            p = Produto(
                self.inputs_estoque['e_nome'].get(),
                float(self.inputs_estoque['e_pcompra'].get()),
                float(self.inputs_estoque['e_pvenda'].get()),
                self.inputs_estoque['e_venc'].get(),
                int(self.inputs_estoque['e_qtd'].get())
            )
            self.estoque.adicionar_produto(p)
            self._atualizar_lista_produtos_venda()
            messagebox.showinfo("Sucesso", "Produto registrado no estoque!")
        except Exception as e:
            messagebox.showerror("Erro", f"Dados inválidos: {e}")

    def processar_venda(self):
        try:
            nome_prod = self.combo_produto_venda.get()
            qtd = int(self.ent_venda_qtd.get())
            pagador = self.ent_venda_pagador.get()
            valor = float(self.ent_venda_valor.get())
            cat = self.combo_cat.get()
            curso = self.combo_curso.get()

            if self.estoque.vender_item(nome_prod, qtd):
                self.consumo.registrar_consumo(pagador, nome_prod, qtd, (valor/qtd))
                
                novo_pgto = Pagamento(pagador, cat, curso, valor)
                novo_pgto.produto_comprado = f"{qtd}x {nome_prod}"
                
                self.pagamentos.registrar_pagamento(novo_pgto)
                
                self._atualizar_lista_produtos_venda()
                messagebox.showinfo("Venda", "Venda finalizada com sucesso!")
            else:
                messagebox.showwarning("Erro", "Quantidade insuficiente em estoque!")
        except Exception as e:
            messagebox.showerror("Erro", "Preencha todos os campos corretamente.")

    def atualizar_visualizacao_relatorio(self):
        self.txt_area.delete(1.0, tk.END)
        self.txt_area.insert(tk.END, f"{'='*110}\nSISTEMA DE GESTÃO CANTINA FATEC - {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n{'='*110}\n\n")
        

        self.txt_area.insert(tk.END, ">> [ESTOQUE] POSIÇÃO DETALHADA:\n")
        self.txt_area.insert(tk.END, f"{'Produto':<25} | {'Qtd':<5} | {'P.Compra':<10} | {'P.Venda':<10} | {'Subtotal Venda'}\n")
        self.txt_area.insert(tk.END, "-"*110 + "\n")
        
        atual = self.estoque.head
        total_patrimonio = 0.0
        while atual:
            subtotal = atual.quantidade * atual.preco_venda
            total_patrimonio += subtotal
            linha = f"{atual.nome:<25} | {atual.quantidade:<5} | R${atual.preco_compra:<8.2f} | R${atual.preco_venda:<8.2f} | R${subtotal:.2f}\n"
            self.txt_area.insert(tk.END, linha)
            atual = atual.proximo
        self.txt_area.insert(tk.END, f"\nTOTAL EM MERCADORIA: R${total_patrimonio:.2f}\n\n" + "="*110 + "\n\n")

        
        self.txt_area.insert(tk.END, ">> [PAGAMENTOS] HISTÓRICO DE VENDAS:\n")
        self.txt_area.insert(tk.END, f"{'Data/Hora':<16} | {'Pagador':<15} | {'Item':<20} | {'Curso/Cat':<20} | {'Valor'}\n")
        self.txt_area.insert(tk.END, "-"*110 + "\n")
        
        pg = self.pagamentos.head
        soma_caixa = 0.0
        while pg:
            
            produto_info = getattr(pg, 'produto_comprado', 'N/A')
            data_str = pg.data_hora.strftime("%d/%m %H:%M")
            linha_pg = f"{data_str:<16} | {pg.pagador:<15} | {produto_info:<20} | {pg.curso}/{pg.categoria[0]:<11} | R${pg.valor:.2f}\n"
            self.txt_area.insert(tk.END, linha_pg)
            soma_caixa += pg.valor
            pg = pg.proximo
            
        self.txt_area.insert(tk.END, f"\nTOTAL EM CAIXA: R${soma_caixa:.2f}\n")

    def salvar_dados_sistema(self):
        SalvarDados.salvar_estoque(self.estoque)
        messagebox.showinfo("Backup", "Dados salvos com sucesso.")

    def carregar_dados_sistema(self):
        try:
            self.estoque = CarregarDados.carregar_estoque()
            self._atualizar_lista_produtos_venda()
            messagebox.showinfo("Sucesso", "Dados carregados.")
        except:
            messagebox.showerror("Erro", "Falha ao carregar backup.")

    def gerar_faker_seguro(self):
        gerador = GeradorDados()
        lote = gerador.gerar_estoque_aleatorio(5)
        atual = lote.head
        while atual:
            self.estoque.adicionar_produto(Produto(atual.nome, atual.preco_compra, atual.preco_venda, atual.data_vencimento, atual.quantidade))
            atual = atual.proximo
        self._atualizar_lista_produtos_venda()
        messagebox.showinfo("Faker", "Dados de teste gerados.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CantinaApp(root)
    root.mainloop()