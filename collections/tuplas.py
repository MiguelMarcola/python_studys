class ContaCorrente():
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self) -> str:
        return f"[>>Código {self.codigo} Saldo {self.saldo}<<]"


conta_gui = ContaCorrente(15)

print(conta_gui)

conta_gui.deposita(500)
print(conta_gui)


conta_dani = ContaCorrente(4568)

print(conta_dani)

conta_dani.deposita(1000)
print(conta_dani)

contas = [conta_gui, conta_dani]
print(contas)

for conta in contas:
    print(conta)

contas = [conta_gui, conta_dani, conta_gui]
print(contas[0])

conta_gui.deposita(100)
print(contas[0])
print(conta_gui)
print(contas[2])


contas[2].deposita(300)
print(conta_gui)
