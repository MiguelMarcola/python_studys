from operator import attrgetter
from equal import ContaSalario

idades = [15, 87, 65, 56, 42, 30, 10, 87]

for i in range(len(idades)):
    print(i, idades[i])

print(list(range(len(idades))))
print(list(enumerate(idades)))

for indice, idade in enumerate(idades):
    print(indice, "x", idade)


usuarios = [
    ("Guilherme", 37, 1981),
    ("Daniela", 24, 1998),
    ("Paulo", 39, 1979)
]

for nome, idade, nacsimento in usuarios:
    print(nome)


for nome, _, _ in usuarios:
    print(nome)


print(sorted(idades))
print(list(reversed(idades)))
print(sorted(idades, reverse=True))

idades.sort()
print(idades)

nomes = ["Guilherme", "Daniela", "Paulo"]
print(sorted(nomes))


conta_gui = ContaSalario(1)
conta_gui.deposito(1000)

conta_dani = ContaSalario(2)
conta_dani.deposito(100)

conta_paulo = ContaSalario(3)
conta_paulo.deposito(300)

contas = [conta_gui, conta_dani, conta_paulo]


def extrai_saldo(conta):
    return conta.saldo


for conta in sorted(contas, key=extrai_saldo):
    print(conta)


for conta in sorted(contas, key=attrgetter("saldo")):
    print(conta)
