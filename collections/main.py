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

# idades.clear()

print(idades)

28 in idades

if 18 in idades:
    idades.remove(18)


idades.insert(0, 20)
print(idades)


idades.extend([19, 14])
print(idades)


idades_no_ano_que_vem = []

for idade in idades:
    idades_no_ano_que_vem.append(idade + 1)

print(idades_no_ano_que_vem)


idades_no_ano_que_vem_2 = [(idade+1) for idade in idades]
print(idades_no_ano_que_vem_2)


teste = [idade for idade in idades if idade > 21]
print(teste)


def proximo_ano(idade):
    return idade + 1


print([proximo_ano(idade) for idade in idades if idade > 21])
