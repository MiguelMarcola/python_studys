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


def deposita_para_todas(contas):
    for conta in contas:
        conta.deposita(100)


contas = [conta_gui, conta_dani]
deposita_para_todas(contas)
for conta in contas:
    print(conta)


contas.insert(0, 76)
print(contas[0], contas[1], contas[2])


# deposita_para_todas(contas)
# print(contas[0], contas[1], contas[2])
# Error for int in position 0

guilherme = ("Guilherme", 37, 1981)  # Tupla
dani = ("Daniela", 24, 1998)  # Tupla
# paulo = (39, "Paulo", 1979) # ruim


usuarios = [guilherme, dani]

usuarios.append(("Paulo", 39, 1987))
print(usuarios)

contas = (conta_gui, conta_dani)
for conta in contas:
    print(conta)

# contas.append("qlq coisa") # Erro elemento imutável

contas[0].deposita(1000)
print(contas[0])
