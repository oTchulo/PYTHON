import os
from datetime import datetime
from collections import Counter
from tabulate import tabulate

ARQUIVO_DADOS = "dados.txt"

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def carregar_dados():
    if not os.path.exists(ARQUIVO_DADOS):
        return []
    dados = []
    try:
        with open(ARQUIVO_DADOS, "r") as f:
            for linha in f:
                partes = linha.strip().split(";")
                if len(partes) == 9:
                    dados.append(partes)
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")
    return dados

def salvar_dados(dados):
    try:
        with open(ARQUIVO_DADOS, "w") as f:
            for d in dados:
                f.write(";".join(d) + "\n")
    except Exception as e:
        print(f"Erro ao salvar dados: {e}")

def adicionar_passageiro():
    limpar_tela()
    while True:
        cpf = input("CPF (apenas números, 11 dígitos): ")
        if cpf.isdigit() and len(cpf) == 11:
            break
        else:
            print("CPF inválido. Deve conter 11 dígitos numéricos.")

    dados = carregar_dados()
    if any(d[0] == cpf for d in dados):
        print("CPF já cadastrado.")
        return

    nome = input("Nome: ")
    destino = input("Destino: ")
    companhia = input("Companhia: ")

    while True:
        preco = input("Preço: ")
        try:
            float(preco)
            break
        except ValueError:
            print("Preço inválido. Digite um número (use ponto para decimais).")

    while True:
        data = input("Data do voo (dd/mm/aaaa): ")
        try:
            datetime.strptime(data, "%d/%m/%Y")
            break
        except ValueError:
            print("Data inválida. Use o formato dd/mm/aaaa.")

    while True:
        hora_saida = input("Hora de Saída (hh:mm): ")
        try:
            datetime.strptime(hora_saida, "%H:%M")
            break
        except ValueError:
            print("Hora de saída inválida. Use o formato hh:mm.")

    while True:
        hora_chegada = input("Hora de Chegada (hh:mm): ")
        try:
            datetime.strptime(hora_chegada, "%H:%M")
            break
        except ValueError:
            print("Hora de chegada inválida. Use o formato hh:mm.")

    num_voo = input("Número do Voo: ")

    dados.append([cpf, nome, destino, companhia, preco, data, hora_saida, hora_chegada, num_voo])
    salvar_dados(dados)
    print("Passageiro adicionado com sucesso!")

def consultar_passagem():
    limpar_tela()
    cpf = input("Informe o CPF: ")
    dados = carregar_dados()
    for d in dados:
        if d[0] == cpf:
            headers = ["CPF", "Nome", "Destino", "Companhia", "Preço", "Data", "Saída", "Chegada", "Voo"]
            print(tabulate([d], headers=headers, tablefmt="grid"))
            return
    print("Passageiro não encontrado.")

def remover_passageiro():
    limpar_tela()
    cpf = input("Informe o CPF: ")
    dados = carregar_dados()
    novos_dados = [d for d in dados if d[0] != cpf]
    if len(novos_dados) == len(dados):
        print("Passageiro não encontrado.")
    else:
        salvar_dados(novos_dados)
        print("Passageiro removido com sucesso.")

def relatorio_passageiros():
    limpar_tela()
    dados = carregar_dados()
    if not dados:
        print("Nenhum passageiro cadastrado.")
        return
    headers = ["CPF", "Nome", "Destino", "Companhia", "Preço", "Data", "Saída", "Chegada", "Voo"]
    print(tabulate(dados, headers=headers, tablefmt="fancy_grid"))

def relatorio_financeiro():
    limpar_tela()
    dados = carregar_dados()
    if not dados:
        print("Nenhum dado financeiro disponível.")
        return
    gastos = {}
    total_geral = 0
    for d in dados:
        nome = d[1]
        try:
            preco = float(d[4])
            total_geral += preco
        except ValueError:
            preco = 0
        gastos[nome] = gastos.get(nome, 0) + preco
    tabela = [[nome, f"R$ {total:.2f}"] for nome, total in gastos.items()]
    print(tabulate(tabela, headers=["Nome", "Total Gasto"], tablefmt="github"))
    print(f"\n→ Soma Total Geral: R$ {total_geral:.2f}")

def destinos_frequentes():
    limpar_tela()
    dados = carregar_dados()
    if not dados:
        print("Nenhum dado de destino disponível.")
        return
    destinos = [d[2] for d in dados]
    contagem = Counter(destinos)
    tabela = [[destino, freq] for destino, freq in contagem.most_common()]
    print(tabulate(tabela, headers=["Destino", "Quantidade"], tablefmt="rounded_grid"))

def menu():
    while True:
        limpar_tela()
        print("====== MENU ======")
        print("1) Adicionar Passageiro")
        print("2) Consultar Passagem")
        print("3) Remover Passageiro")
        print("4) Relatório de Passageiros")
        print("5) Relatório Financeiro")
        print("6) Destinos Frequentes")
        print("0) Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            adicionar_passageiro()
        elif opcao == "2":
            consultar_passagem()
            input("\nPressione ENTER para voltar ao menu.")
        elif opcao == "3":
            remover_passageiro()
            input("\nPressione ENTER para voltar ao menu.")
        elif opcao == "4":
            relatorio_passageiros()
            input("\nPressione ENTER para voltar ao menu.")
        elif opcao == "5":
            relatorio_financeiro()
            input("\nPressione ENTER para voltar ao menu.")
        elif opcao == "6":
            destinos_frequentes()
            input("\nPressione ENTER para voltar ao menu.")
        elif opcao == "0":
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida.")
            input("\nPressione ENTER para tentar novamente.")

if __name__ == "__main__":
    menu()
