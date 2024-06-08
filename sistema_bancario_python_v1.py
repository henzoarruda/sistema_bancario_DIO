menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == '1':
        valor = float(input("Informe o valor de depósito:"))
        if valor >= 0:
            saldo += valor
            extrato += f'Depósito realizado: R$ {valor:,.2f}\n'
        else:
            print("Operação falhou! O valor inserido é inválido")

    elif opcao == '2':
        valor = float(input("Informe o valor que deseja sacar:"))
        if valor >= 0:
            saldo -= valor
            extrato += f'Saque realizado: R$ {valor:,.2f}\n'
            numero_saques += 1
            if numero_saques > LIMITE_SAQUES:
                print("Limite de saques excedido")
        else:
            print("Operação falhou! O valor inserido é inválido")

    elif opcao == '3':
        print(f"Seu saldo atual é de: R$ {saldo:,.2f}")
        print("Extrato Bancário:")
        print(extrato)

    elif opcao == '4':
        print("Saindo...")
        break
        
    else:
        print("Opção inválida!")
