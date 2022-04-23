class ContaSalario:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposito(self, valor):
        self.saldo += valor

    def __str__(self):
        return f">>Código {self.codigo} Saldo {self.saldo}<<"

    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False
        return self.codigo == outro.codigo and self.saldo == outro.saldo

    def __lt__(self, outro):
        return self.saldo < outro.saldo


conta1 = ContaSalario(37)
conta1.deposito(100)
print(conta1)

conta2 = ContaSalario(37)
print(conta2)

print(conta1 == conta2)
print(conta1 in [conta2])
print(conta2 in [conta1])

conta1.deposito(100)
print(conta1 == conta2)
print(conta1 in [conta2])
print(conta2 in [conta1])
