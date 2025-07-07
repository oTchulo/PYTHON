import os

class Cores:
    Vermelho = '\033[91m'
    Verde = '\033[92m'
    Amarelo = '\033[93m'
    Azul = '\033[94m'
    Reset = '\033[0m'

Titulo = """
\033[96m
========================================
               𝐁𝐈𝐍𝐍
========================================
\033[0m
"""

# Diárias 
valores_tipo1 = [20.00, 28.00, 35.00, 42.00, 48.00, 53.00]
valores_tipo2 = [25.00, 34.00, 42.00, 50.00, 57.00, 63.00]

continuar = True
while continuar:
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa tela (Windows ou Linux/Mac)
    print(Titulo)

    # Entrada
    NOME = input("Digite seu nome: ")

    # Validação do CPF (deve ter exatamente 11 números)
    while True:
        CPF = input("Digite seu CPF (somente números, 11 dígitos): ")
        if len(CPF) == 11 and CPF.isdigit():
            break
        else:
            print(Cores.Vermelho + "CPF inválido! Digite exatamente 11 números." + Cores.Reset)

    while True:
        try:
            pessoas = int(input("Digite o número de pessoas (1 a 6): "))
            if 1 <= pessoas <= 6:
                break
            else:
                print(Cores.Vermelho + "Número inválido. Deve estar entre 1 e 6." + Cores.Reset)
        except ValueError:
            print(Cores.Vermelho + "Digite um número inteiro válido." + Cores.Reset)

    # Informações dos quartos
    print("\nTemos duas opções de apartamento disponíveis para sua estadia:\n")

    print(Cores.Azul + "Tipo 1 - Conforto Essencial:" + Cores.Reset)
    print("  - Ideal para quem busca economia sem abrir mão do bem-estar.")
    print("  - Acomodações simples, aconchegantes e funcionais.")
    print("  - Incluso no quarto:")
    print("     • Cama box casal ou solteiro")
    print("     • TV LED 32'' com canais abertos")
    print("     • Ventilador de teto")
    print("     • Banheiro privativo")
    print("     • Wi-Fi gratuito\n")

    print(Cores.Azul + "Tipo 2 - Luxo Premium:" + Cores.Reset)
    print("  - Perfeito para quem deseja uma experiência mais completa e confortável.")
    print("  - Acomodações mais espaçosas, com acabamento refinado.")
    print("  - Incluso no quarto:")
    print("     • Cama king size com enxoval premium")
    print("     • TV Smart 50'' com streaming liberado")
    print("     • Ar-condicionado split")
    print("     • Frigobar abastecido")
    print("     • Banheiro com ducha a gás e amenities exclusivos")
    print("     • Serviço de quarto incluso")
    print("     • Wi-Fi de alta velocidade\n")

    while True:
        tipo = input("Escolha um tipo de apartamento (1 ou 2): ")
        if tipo in ['1', '2']:
            tipo = int(tipo)
            break
        else:
            print(Cores.Vermelho + "Número inválido. Digite apenas 1 ou 2." + Cores.Reset)

    while True:
        try:
            dias = int(input("Digite o número de dias de estadia: "))
            if dias > 0:
                break
            else:
                print(Cores.Vermelho + "Digite um número de diária válido (maior que 0)." + Cores.Reset)
        except ValueError:
            print(Cores.Vermelho + "Digite um número inteiro válido." + Cores.Reset)

    indice = pessoas - 1  # Corrigido: listas começam no índice 0
    if tipo == 1:
        diaria = valores_tipo1[indice]
    else:
        diaria = valores_tipo2[indice]

    total = diaria * pessoas * dias

    # Processamento 
    print("\n" + Cores.Amarelo + "=" * 40 + Cores.Reset)
    print(Cores.Verde + "   RELATÓRIO DE RESERVA    " + Cores.Reset)
    print(Cores.Amarelo + "=" * 40 + Cores.Reset)
    print(f"Nome: {NOME}")
    print(f"CPF: {CPF}")
    print(f"Número de Pessoas: {pessoas}")
    print(f"Tipo de apartamento: {tipo}")
    print(f"Dias de estadia: {dias}")
    print(f"Valor da diária por pessoa: R$ {diaria:.2f}")
    print(Cores.Verde + f"Valor total da Estadia: R$ {total:.2f}" + Cores.Reset)
    print(Cores.Amarelo + "=" * 40 + Cores.Reset)

    while True:
        opcao = input("\nDeseja fazer outra reserva? (sim/não): ").lower()
        if opcao == 'sim':
            continuar = True
            break
        elif opcao == 'não':
            continuar = False
            print(Cores.Azul + "\nObrigado por usar o sistema BINN. Volte sempre!" + Cores.Reset)
            break
        else:
            print(Cores.Vermelho + "Resposta inválida! Digite 'sim' ou 'não'." + Cores.Reset)