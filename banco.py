saldo = 0
saques_realizados = []
depositos_realizados = []

def sacar(valor):
    global saldo, saques_realizados
    if saldo >= valor and len(saques_realizados) < 3 and valor <= 500:
        saldo -= valor
        saques_realizados.append(valor)
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
    elif saldo < valor:
        print("Saldo insuficiente.")
    elif len(saques_realizados) >= 3:
        print("Limite máximo de saques diários atingido.")
    else:
        print("Valor de saque inválido.")

def depositar(valor):
    global saldo, depositos_realizados
    if valor > 0:
        saldo += valor
        depositos_realizados.append(valor)
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Valor de depósito inválido.")

def extrato():
    global saldo, saques_realizados, depositos_realizados
    print("Extrato:")
    if not saques_realizados and not depositos_realizados:
        print("Não foram realizadas movimentações.")
    else:
        for saque in saques_realizados:
            print(f"Saque: R$ {saque:.2f}")
        for deposito in depositos_realizados:
            print(f"Depósito: R$ {deposito:.2f}")
    print(f"Saldo atual: R$ {saldo:.2f}")

def exibir_menu():
    print("\n===== Sistema Bancário DIO =====")
    print("1. Sacar")
    print("2. Depositar")
    print("3. Visualizar Extrato")
    print("4. Sair\n")

while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor_saque = float(input("Digite o valor do saque: "))
        sacar(valor_saque)
    elif opcao == "2":
        valor_deposito = float(input("Digite o valor do depósito: "))
        depositar(valor_deposito)
    elif opcao == "3":
        extrato()
    elif opcao == "4":
        print("Saindo do sistema bancário...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.\n")
