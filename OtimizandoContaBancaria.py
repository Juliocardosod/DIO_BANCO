class Cliente:
    def __init__(self, cpf, nome, endereco, data_nascimento):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco
        self.data_nascimento = data_nascimento

class ContaBancaria:
    def __init__(self, saldo_inicial=0, cliente=None):
        self.saldo = saldo_inicial
        self.saques_diarios = 0
        self.saques_total = 0
        self.saques_valor_total = 0
        self.cliente = cliente

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            return f"Depósito de {valor:.2f} BRL realizado. Novo saldo: {self.saldo:.2f} BRL"
        else:
            return "Valor de depósito inválido. Por favor, insira um valor positivo."

    def saque(self, valor):
        if valor > 0 and valor <= 500:
            if self.saldo >= valor:
                if self.saques_diarios < 3:
                    self.saldo -= valor
                    self.saques_diarios += 1
                    self.saques_total += 1
                    self.saques_valor_total += valor
                    return f"Saque de {valor:.2f} BRL realizado. Novo saldo: {self.saldo:.2f} BRL"
                else:
                    return "Limite diário de saques atingido. Tente novamente amanhã."
            else:
                return "Saldo insuficiente para realizar o saque."
        else:
            return "Valor de saque inválido. O valor máximo de saque é 500 BRL."

    def extrato(self):
        return f"Saldo da conta: {self.saldo:.2f} BRL\nSaques diários realizados: {self.saques_diarios}\nTotal de saques realizados: {self.saques_total}\nValor total sacado: {self.saques_valor_total:.2f} BRL"

def criar_cliente(cpf, nome, endereco, data_nascimento):
    for cliente in clientes:
        if cliente.cpf == cpf:
            return "CPF já cadastrado. Escolha outro CPF."
    novo_cliente = Cliente(cpf, nome, endereco, data_nascimento)
    clientes.append(novo_cliente)
    return f"Cliente {nome} cadastrado com sucesso!"

clientes = [] 

def criar_conta_corrente(cliente, saldo_inicial=0):
    conta = ContaBancaria(saldo_inicial, cliente)
    return conta

def exibir_menu():
    print("\nMenu:")
    print("1 - Criar cliente")
    print("2 - Criar conta corrente")
    print("0 - Sair")

def exibir_menu2():
    print("\nMenu:")
    print("1 - Realizar depósito")
    print("2 - Realizar saque")
    print("3 - Exibir extrato")
    print("0 - Sair")

clientes = []
loop = True

while True:
    exibir_menu()
    opcao = input("Digite a opção desejada: ")

    if opcao == "1":#Criar cliente
        cpf = input("Digite o CPF do cliente: ")
        nome = input("Digite o nome do cliente: ")
        endereco = input("Digite o endereço do cliente: ")
        data_nascimento = input("Digite a data de nascimento do cliente: ")
        print(criar_cliente(cpf, nome, endereco, data_nascimento))

    elif opcao == "2":#Criar conta
        cpf_cliente = input("Digite o CPF do cliente associado à conta: ")
        saldo_inicial = float(input("Digite o saldo inicial da conta: "))
        cliente_associado = None
        for cliente in clientes:
            if cliente.cpf == cpf_cliente:
                cliente_associado = cliente
                break
        if cliente_associado:
            conta = criar_conta_corrente(cliente_associado, saldo_inicial)
            print(f"Conta criada para o cliente {cliente_associado.nome}.")
            while True:
                exibir_menu2()
                opcao = input("Digite a opção desejada: ")
                if opcao == "1":
                    valor = float(input("DIgite o valor do depósito: "))
                    ContaBancaria.deposito(conta, valor)
                elif opcao == "2":
                    valor = float(input("Digite o valor do saque: "))
                    ContaBancaria.saque(conta, valor)
                elif opcao == "3":
                    print(ContaBancaria.extrato(conta))
                elif opcao == "0":
                    break
                else:
                    print("Opção inválida. Tente novamente.")

        else:
            print("Cliente não encontrado. Cadastre o cliente primeiro.")

        cpf = input("Digite o CPF do cliente: ")

    elif opcao == "0":
        print("Saindo do programa. Obrigado!")
        break

    else:
        print("Opção inválida. Tente novamente.")

