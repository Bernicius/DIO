class Usuario:
    def __init__(self, nome, cpf, data_nascimento, logradouro):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.logradouro = logradouro

class Conta:
    LIMITE_SAQUES = 3
    
    def __init__(self, numero_conta, usuario, saldo=0):
        self.agencia = "0001"
        self.numero_conta = numero_conta
        self.usuario = usuario
        self.saldo = saldo
        self.extrato = ""
        self.numero_saques = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")
    
    def sacar(self, valor, limite):
        excedeu_saldo = valor > self.saldo
        excedeu_limite = valor > limite
        excedeu_saques = self.numero_saques >= Conta.LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            self.saldo -= valor
            self.extrato += f"Saque: R$ {valor:.2f}\n"
            self.numero_saques += 1
            print("Saque realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    def exibir_extrato(self):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not self.extrato else self.extrato)
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("==========================================")

class Banco:
    def __init__(self):
        self.usuarios = []
        self.contas = []
        self.limite = 500

    def cadastrar_usuario(self):
        nome = input("Informe o nome do usuário: ")
        cpf = input("Informe o CPF (apenas números): ")
        data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
        logradouro = input("Informe o endereço (logradouro, número, bairro, cidade, sigla): ")

        for usuario in self.usuarios:
            if usuario.cpf == cpf:
                print("CPF já cadastrado. Não é possível cadastrar dois usuários com o mesmo CPF.")
                return
        
        usuario = Usuario(nome, cpf, data_nascimento, logradouro)
        self.usuarios.append(usuario)
        print(f"Usuário {nome} cadastrado com sucesso!")
    
    def cadastrar_conta(self):
        cpf = input("Informe o CPF do usuário para a conta: ")
        usuario_encontrado = None
        
        for usuario in self.usuarios:
            if usuario.cpf == cpf:
                usuario_encontrado = usuario
                break

        if usuario_encontrado:
            numero_conta = len(self.contas) + 1
            conta = Conta(numero_conta, usuario_encontrado)
            self.contas.append(conta)
            print(f"Conta número {numero_conta} cadastrada com sucesso para o usuário {usuario_encontrado.nome}!")
        else:
            print("Usuário não encontrado. Cadastre o usuário primeiro.")
    
    def depositar(self):
        numero_conta = int(input("Informe o número da conta: "))
        conta = self.buscar_conta(numero_conta)
        
        if conta:
            valor = float(input("Informe o valor do depósito: "))
            conta.depositar(valor)
        else:
            print("Conta não encontrada.")

    def sacar(self):
        numero_conta = int(input("Informe o número da conta: "))
        conta = self.buscar_conta(numero_conta)

        if conta:
            valor = float(input("Informe o valor do saque: "))
            conta.sacar(valor, self.limite)
        else:
            print("Conta não encontrada.")
    
    def exibir_extrato(self):
        numero_conta = int(input("Informe o número da conta: "))
        conta = self.buscar_conta(numero_conta)

        if conta:
            conta.exibir_extrato()
        else:
            print("Conta não encontrada.")
    
    def buscar_conta(self, numero_conta):
        for conta in self.contas:
            if conta.numero_conta == numero_conta:
                return conta
        return None

def menu():
    return """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [c] Cadastrar Usuário
    [a] Cadastrar Conta
    [q] Sair
    => """

def main():
    banco = Banco()

    while True:
        opcao = input(menu())

        if opcao == "d":
            banco.depositar()
        elif opcao == "s":
            banco.sacar()
        elif opcao == "e":
            banco.exibir_extrato()
        elif opcao == "c":
            banco.cadastrar_usuario()
        elif opcao == "a":
            banco.cadastrar_conta()
        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
