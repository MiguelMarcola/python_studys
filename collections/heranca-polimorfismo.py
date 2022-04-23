from abc import ABCMeta, abstractclassmethod


class Conta(metaclass=ABCMeta):
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self) -> str:
        return f"[>>Código {self._codigo} Saldo {self._saldo}<<]"

    @abstractclassmethod
    def passa_o_mes(self):
        pass


class ContaCorrente(Conta):

    def passa_o_mes(self):
        self._saldo -= 2


class ContaPoupanca(Conta):
    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3


class ContaInvestimento(Conta):
    pass


conta16 = ContaCorrente(16)
conta16.deposita(1000)
print(conta16)

conta17 = ContaPoupanca(17)
conta17.deposita(1000)
print(conta17)

contas = [conta16, conta17]

for conta in contas:
    conta.passa_o_mes()
    print(conta)

# ContaInvestimento(121323)
# Error Can't instantiate abstract class ContaInvestimento with abstract method passa_o_mes
#
