
class ContaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial
        self.saques_diarios = 0
        self.saques_total = 0
        self.saques_valor_total = 0

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


def main():
    saldo_inicial = float(0) #input("Digite o saldo inicial: ")
    conta = ContaBancaria(saldo_inicial)

    while True:
        print("\nOpções:")
        print("S - Saque")
        print("E - Extrato")
        print("D - Depósito")
        print("S - Sair")

        opcao = input("Digite a opção desejada: ").upper()

        if opcao == "S":
            valor_saque = float(input("Digite o valor do saque: "))
            print(conta.saque(valor_saque))
        elif opcao == "E":
            print(conta.extrato())
        elif opcao == "D":
            valor_deposito = float(input("Digite o valor do depósito: "))
            print(conta.deposito(valor_deposito))
        elif opcao == "S":
            print("Saindo do programa. Obrigado!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()