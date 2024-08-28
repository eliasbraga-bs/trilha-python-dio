# Define o menu de opções que será exibido para o usuário
menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

# Inicializa variáveis essenciais para as operações bancárias
saldo = 0 # Saldo inicial da conta
limite = 500 # Limite máximo para saques
extrato = "" # Histórico das operações realizadas
numero_saques = 0 # Contador de saques realizados no dia
LIMITE_SAQUES = 3 # Limite de saques permitidos por dia

# Inicia o loop infinito para manter o programa em execução até o usuário decidir sair
while True:

    # Exibe o menu e lê a opção escolhida pelo usuário
    opcao = input (menu)

    # Caso a opção escolhida seja para depositar
    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor 
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! o valor informado é inválido.")

    # Caso a opção escolhida seja para sacar
    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        # Mensagens de erro dependendo da condição que impede o saque
        if excedeu_saldo:
            print("Operação falou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falou! O valor do sque exvede o limite.") 

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido,")

        # Se todas as verificações forem satisfeitas, realiza o saque
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falou! O valor informado é iválido.")

    # Caso a opção escolhida seja para exibir o extrato
    elif opcao == "3":
        print("\n====================== EXTRATO ======================")
        print("Não foram realizadas movimentação." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")  
        print("====================================================")
    
    # Caso a opção escolhida seja para sair
    elif opcao == "4":
        break

    # Caso o usuário insira uma opção inválida    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")    
                           
