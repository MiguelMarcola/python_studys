from random import randint
import forca


def jogar_adivinhacao():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    tentativas = 0
    numero_secreto = randint(0, 200)
    pontos = 100

    while(tentativas == 0):
        print("Qual o nível de dificuldade?")
        print("(1) Fácil (2) Médio (3) Difícil")

        nivel = int(input("Defina o nível: "))

        if(nivel == 1):
            tentativas = 20
            pontos_perdidos = 5
        elif(nivel == 2):
            tentativas = 10
            pontos_perdidos = 10
        elif(nivel == 3):
            tentativas = 5
            pontos_perdidos = 20
        else:
            print("Valor inválido!\n")

    for rodada in range(1, tentativas + 1):
        chute = input("Digite o seu número: ")
        chute = int(chute)
        print(f"Tentativa {rodada} de {tentativas}")
        print("Você digitou: ", chute)

        if(chute < 0 or chute > 200):
            print("Você deve digitar um número entre 0 e 200!\n\n")
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

    print(f"Fim do jogo! Você fez {pontos} pontos")

    forca.imprime_mensagem_vencedor()


if(__name__ == "__main__"):
    jogar_adivinhacao()
