from random import randint
import forca


def jogar_adivinhacao():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    tentativas = 0
    pontos = 100

    while(tentativas == 0):
        print("Qual o nível de dificuldade?")
        print("(1) Fácil (2) Médio (3) Difícil")

        nivel = int(input("Defina o nível: "))

        if(nivel == 1):
            tentativas = 10
            max_num = 100
            pontos_perdidos = 10
        elif(nivel == 2):
            tentativas = 16
            max_num = 500
            pontos_perdidos = 6.25
            pontos_perdidos = 10
        elif(nivel == 3):
            tentativas = 25
            pontos_perdidos = 4
            max_num = 1000
        else:
            print("Valor inválido!\n")

        numero_secreto = randint(0, max_num)

    for rodada in range(1, tentativas + 1):
        print(f"Tentativa {rodada} de {tentativas}")
        chute = input(f"(0 a {max_num})\nDigite o seu número: ")
        chute = int(chute)

        print("Você digitou: ", chute)

        if(chute < 0 or chute > max_num):
            print(f"Você deve digitar um número entre 0 e {max_num}!\n\n")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou!\n")
            break
        else:
            rodada += 1
            pontos -= pontos_perdidos
            if(maior):
                print("Digite um valor menor!\n")
            elif(menor):
                print("Digite um valor maior!\n")
    if(acertou):
        print(f"Fim do jogo! Você fez {pontos} pontos")

        forca.imprime_mensagem_vencedor()
    else:
        print(f"Fim do jogo! Você fez {pontos} pontos")

        forca.imprime_mensagem_perdedor()


if(__name__ == "__main__"):
    jogar_adivinhacao()
