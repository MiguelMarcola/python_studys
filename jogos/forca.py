from random import randint
from unidecode import unidecode


def jogar_forca():
    mensagem()

    string_velha = gera_palavra()

    palavra_secreta = unidecode(string_velha)

    enforcou = False
    acertou = False
    erros = 0
    letras_chutadas = []

    resposta = palavra_array(palavra_secreta)

    desenha_forca(erros)
    print(f"{erros} erros de 7")
    print(formata_texto(resposta))

    while(not enforcou and not acertou):

        chute = input("\n\nQual letra? ").upper().strip()
        letras_chutadas.append(chute)

        index = 0

        if(chute in palavra_secreta):
            for letra in palavra_secreta:
                if(chute == letra):
                    resposta[index] = letra
                index += 1
        else:
            erros += 1

        desenha_forca(erros)
        print(f"{erros} erros de 7\n")
        print(f"Letras utilizadas: {letras_chutadas}\n\n")
        print(formata_texto(resposta))
        enforcou = erros == 7
        acertou = "_" not in resposta

    if(enforcou):
        imprime_mensagem_perdedor(palavra_secreta)

    if(acertou):
        imprime_mensagem_vencedor()

    print("\n\nFim do jogo!")


def mensagem():
    print("*********************************")
    print("Bem vindo ao jogo de Forca!")
    print("*********************************")


def gera_palavra():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        palavras.append(linha.strip())

    arquivo.close()

    palavra_secreta = palavras[randint(0, len(palavras) - 1)].upper()

    return palavra_secreta


def palavra_array(palavra):
    return ["_" for letra in palavra]


def formata_texto(palavra):
    texto = " ".join(palavra)

    return texto


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if(__name__ == "__main__"):
    jogar_forca()
