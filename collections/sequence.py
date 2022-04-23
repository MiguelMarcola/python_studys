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
