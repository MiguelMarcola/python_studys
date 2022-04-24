from cgi import test
from collections import defaultdict


aparicoes = {
    "Guilherme": 1,
    "cachorro": 2,
    "nome": 2,
    "vindo": 1
}
print(type(aparicoes))
print(aparicoes["Guilherme"])

# print(aparicoes["xpto"])
# Error

print(aparicoes.get("xpto", 0))
print(aparicoes.get("cachorro", 0))


# aparicoes = dict(Guilherme = 2, cachorro = 1)

aparicoes["Carlos"] = 1
print(aparicoes)
aparicoes["Carlos"] = 2
print(aparicoes)
del aparicoes["Carlos"]
print(aparicoes)

print("cachorro" in aparicoes)
print("Carlos" in aparicoes)

for elemento in aparicoes:
    print(elemento)


for elemento in aparicoes.values():
    print(elemento)


for elemento in aparicoes.keys():
    valor = aparicoes[elemento]
    print(elemento, valor)

for elemento in aparicoes.items():
    print(elemento)


for chave, valor in aparicoes.items():
    print(chave, "=", valor)


teste = [f"palavra {chave}" for chave in aparicoes.keys()]
print(teste)


meu_texto = "Bem vindo meu nome é guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
meu_texto = meu_texto.lower()

aparicoes = {}

for palavra in meu_texto.split():
    ate_agora = aparicoes.get(palavra, 0)
    aparicoes[palavra] = ate_agora + 1

print(aparicoes)


aparicoes = defaultdict(int)

for palavra in meu_texto.split():
    ate_agora = aparicoes[palavra]
    aparicoes[palavra] = ate_agora + 1

print(aparicoes)
