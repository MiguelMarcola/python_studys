idades = [31, 36, 24, 18]

print(idades)
type(idades)
len(idades)
idades[0]

idades.append(15)

for idade in idades:
    print(idade)


# idades.remove(30)

idades.append(31)
idades.remove(31)

print(idades)

idades.clear()

print(idades)
