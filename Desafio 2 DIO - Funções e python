def menu():
    return """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [c] Cadastrar Usuário
    [a] Cadastrar Conta
    [q] Sair
    => """

def depositar(contas, numero_conta, valor):
    for conta in contas:
        if conta['numero_conta'] == numero_conta:
            if valor > 0:
                conta['saldo'] += valor
                conta['extrato'] += f"Depósito: R$ {valor:.2f}\n"
                print("Depósito realizado com sucesso!")
            else:
                print("Operação falhou! O valor informado é inválido.")
            return contas
    print("Conta não encontrada.")
    return contas

def sacar(*, contas, limite, LIMITE_SAQUES):
    numero_conta = int(input("Informe o número da conta: "))
    for conta in contas:
        if conta['numero_conta'] == numero_conta:
            valor = float(input("Informe o valor do saque: "))
            excedeu_saldo = valor > conta['saldo']
            excedeu_limite = valor > limite
            excedeu_saques = conta['numero_saques'] >= LIMITE_SAQUES

            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")
            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")
            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido.")
            elif valor > 0:
                conta['saldo'] -= valor
                conta['extrato'] += f"Saque: R$ {valor:.2f}\n"
                conta['numero_saques'] += 1
                print("Saque realizado com sucesso!")
            else:
                print("Operação falhou! O valor informado é inválido.")
            return contas
    print("Conta não encontrada.")
    return contas

def exibir_extrato(contas, numero_conta):
    for conta in contas:
        if conta['numero_conta'] == numero_conta:
            print("\n================ EXTRATO ================")
            print("Não foram realizadas movimentações." if not conta['extrato'] else conta['extrato'])
            print(f"\nSaldo: R$ {conta['saldo']:.2f}")
            print("==========================================")
            return
    print("Conta não encontrada.")

def cadastrar_usuario(usuarios):
    nome = input("Informe o nome do usuário: ")
    cpf = input("Informe o CPF (apenas números): ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    logradouro = input("Informe o endereço (logradouro, número, bairro, cidade, sigla): ")

    # Verifica se o CPF já está cadastrado
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("CPF já cadastrado. Não é possível cadastrar dois usuários com o mesmo CPF.")
            return usuarios

    usuarios.append({
        "nome": nome,
        "cpf": cpf,
        "data_nascimento": data_nascimento,
        "logradouro": logradouro
    })
    print(f"Usuário {nome} cadastrado com sucesso!")
    return usuarios

def cadastrar_conta(contas, usuarios):
    cpf = input("Informe o CPF do usuário para a conta: ")
    usuario_encontrado = None
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            usuario_encontrado = usuario
            break

    if usuario_encontrado:
        numero_conta = len(contas) + 1
        conta = {
            "agencia": "0001",
            "numero_conta": numero_conta,
            "usuario": usuario_encontrado,
            "saldo": 0,
            "extrato": "",
            "numero_saques": 0
        }
        contas.append(conta)
        print(f"Conta número {numero_conta} cadastrada com sucesso para o usuário {usuario_encontrado['nome']}!")
    else:
        print("Usuário não encontrado. Cadastre o usuário primeiro.")
    return contas

def main():
    limite = 500
    LIMITE_SAQUES = 3
    usuarios = []
    contas = []

    while True:
        opcao = input(menu())

        if opcao == "d":
            numero_conta = int(input("Informe o número da conta: "))
            valor = float(input("Informe o valor do depósito: "))
            contas = depositar(contas, numero_conta, valor)
        elif opcao == "s":
            contas = sacar(contas=contas, limite=limite, LIMITE_SAQUES=LIMITE_SAQUES)
        elif opcao == "e":
            numero_conta = int(input("Informe o número da conta: "))
            exibir_extrato(contas, numero_conta)
        elif opcao == "c":
            usuarios = cadastrar_usuario(usuarios)
        elif opcao == "a":
            contas = cadastrar_conta(contas, usuarios)
        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
