def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular,
             "saldo": saldo, "limite": limite}
    return conta


def depositar(conta, valor):
    conta["saldo"] += valor
    return conta


def sacar(conta, valor):
    conta["saldo"] -= valor
    return conta


def extrato(conta):
    print("O saldo da sua conta é {}".format(conta["saldo"]))


conta = cria_conta(12334, "Miguel", 1000, 10000)
extrato(conta)

conta = depositar(conta, 1500)
extrato(conta)

conta = sacar(conta, 500)
extrato(conta)
