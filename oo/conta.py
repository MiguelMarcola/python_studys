class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco = "001"

    def depositar(self, valor):
        self.__saldo += valor
        print(f"depósito de U$ {valor:,.2f} efetuado")
        self.extrato()

    def __pode_sacar(self, valor_saque):
        valor_disponivel = self.__saldo + self.__limite
        return valor_disponivel >= valor_saque

    def sacar(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
            print(f"saque de U$ {valor:,.2f} efetuado")
            self.extrato()
        else:
            print(f"Você não possui saldo suficiente!")

    def extrato(self):
        print(f"O saldo da sua conta é U$ {self.__saldo:,.2f}")

    def tranferencia(self, valor, recebedor):
        self.__saldo -= valor
        recebedor.__saldo += valor
        print(
            f"Trasferência de U$ {valor:,.2f} para o {recebedor.__titular} realizada com sucesso!")
        self.extrato()

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    @property
    def limite(self):
        print("Chamando o @property")
        return self.__limite

    @staticmethod
    def codigo_banco():
        print("Chamando o @staticmethod")
        return "001"

    @staticmethod
    def codigo_bancos():
        print("Chamando o @staticmethod")
        return {"BB": "001", "Caixa": "104", "Bradesco": "237"}

    @limite.setter
    def limite(self, limite):
        print("Chamando o @property")
        self.__limite = limite


# conta = Conta(123, "Miguel", 5000, 10000)

# conta2 = Conta(1234, "Joo", 0, 100000)

# conta.depositar(1500)

# conta.sacar(50000)

# conta.tranferencia(500, conta2)

# conta2.extrato()

# print(conta.limite)

# conta.limite = 5000

# print(conta.limite)

# codigos = Conta.codigo_bancos()

# print(codigos)
