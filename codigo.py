import random

palavras = ['python', 'html', 'java script', 'c++', 'programacao']

def jogar():
    palavra = random.choice(palavras)
    letras = ['_'] * len(palavra)
    tentativas = 4
    erradas = []

    while tentativas > 0:
        print('Palavra:', ' '.join(letras))
        print('Tentativas:', tentativas)
        print('Letras erradas:', erradas)
        letra = input('Digite uma letra e tente a sorte: ')

        if letra in letras or letra in erradas:
            print('Você já tentou essa letra seu frango, preste atenção.')
            continue

        if letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    letras[i] = letra
        else:
            tentativas -= 1
            erradas.append(letra)
            print('Errou frango, você nunca aprende!')

        if '_' not in letras:
            print('Boa galizé! A palavra era:', palavra)
            break
    else:
        print('Você perdeu frango, vai arregar? A palavra era:', palavra)

jogar()
