# Projeto Cantina Fatec 
Sistema de gestão desenvolvido para as disciplinas de Estrutura de Dados e Linguagem de Programação 2. O objetivo é controlar o estoque e as vendas da cantina da Atlética da Fatec Rio Claro.

## O que o sistema faz:
* Controle de Estoque: Cadastra produtos e prioriza a venda dos itens mais antigos (perecíveis).
* Gestão de Vendas: Registra pagamentos via PIX, identificando quem comprou (aluno, professor ou servidor).
* Baixa Automática: Ao realizar uma venda, o sistema atualiza o estoque e gera um registro de consumo.
* Relatórios: Gera histórico de vendas e de consumo.

## Como Rodar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/naumsarti/Cantina_FATEC_2026.git

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt

3. **Execute o sistema**
   ```bash
   python main.py
