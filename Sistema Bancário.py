menu = """ 

[1] Depositar
[2] Saque
[3] Extrato
[0] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor que deseja depositar\n"))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            
            print("\nDeposito efetuado com sucesso!")
            print(f"\nSaldo: R$ {saldo: .2f}\n")
        else:
            print("A operação falhou, o valor informado é inválido")

    elif opcao == "2":
        valor = float(input("informe o valor que deseja sacar\n"))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! vocÊ não tem saldo suficiente")

        if excedeu_limite:    
            print("Operação falhou! valor do saque excedeu o limite por transação")

        if excedeu_saques:
            print("Operação falhou! você excedeu o limite de saques diários")  

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor: .2f}\n"
            numero_saques += 1

            print("\nSaque efetuado com sucesso!")
            print(f"\nSaldo: R$ {saldo: .2f}\n")

        else:
            print("Operação falhou! o valor informado é inválido")    

    elif opcao == "3":
        print("\n============ EXTRATO ============\n")
        print("\nNão foram realizadas movimentações na conta\n" "\n"if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo: .2f}")
        print("===================================")

    elif opcao == "0":
        break

    else:
        print("Operação inválida, por favor selecione uma opcao válida")




