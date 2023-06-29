import random
def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavras = []

    with open("frutas.txt", "r") as arquivo:

        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero]

    letras_certas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    tentativa = 0

    print(letras_certas)

    while not enforcou and not acertou:
        chute = input("Digite uma letra: ").lower().strip()
        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if letra == chute:
                    letras_certas[index] = letra
                index += + 1
        else:
            tentativa += 1
        enforcou = tentativa == 6
        acertou = "_" not in letras_certas
        print(letras_certas)
    if acertou:
        print("Voce Ganhou!!!")
    else:
        print("Perdeu, Tente Novamente")

    print("Fim do jogo")


if (__name__ == "__main__"):
    jogar()
