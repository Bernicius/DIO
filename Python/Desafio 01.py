def deposito(valor, saldo):
    saldo += valor
    extrato(saldo)
    return saldo

def saque(valor, saldo):
    if valor < saldo:
        saldo -= valor
        extrato(saldo)
        return saldo
    else:
        print(f"Valor inválido")

def validar_saldo(saldo):
    while saldo < 0:
        saldo = float(input("Digite um saldo válido R$:"))
    return saldo

def menu():
    print("""\t\t[1]Depositar
    \t[2]Sacar
    \t[3]Mostrar extrato
    \t[4]Encerrar programa""")

def extrato(saldo):
    print("====================================\n")
    print(f"Saldo Bancário R$:{saldo:.2f}")
    print("\n====================================")

def validar_limite(valor):
    if valor > 500:
        print("Montante inválido, você não tem limite para este saque")
        return 0
    else:
        return valor

LIMITE_SAQUE = 3
op = 0
saldo_inicial = 0
quantidade_saque = 0  

while op != 4:
    menu()
    op = int(input("Digite uma opcao:"))
    if op == 1:
        valor = float(input("Digite o valor:"))
        validar_saldo(valor)
        saldo_inicial = deposito(valor, saldo_inicial)
    if op == 2:
        valor = float(input("Digite o valor:"))
        validar_saldo(valor)
        if saldo_inicial == 0:
            print("Saldo insuficiente!")
            extrato(saldo_inicial)
        else:
            if quantidade_saque < LIMITE_SAQUE:
                if(validar_limite(valor) != 0):
                    saldo_inicial = saque(valor, saldo_inicial)
                    quantidade_saque += 1
            else:
                print("Excedeu o número de saques")
    if op == 3:
        extrato(saldo_inicial)
    if op == 4:
        print("Programa encerrado!")
