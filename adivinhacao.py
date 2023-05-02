import random

def jogar():
    print('*********************************')
    print('Bem vindo ao jogo de adivinhação!')
    print('*********************************')
3
    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print('Escolha o nível de dificuldade')
    print('1- Fácil 2- Médio 3- Dificil')

    nivel = int(input('Defina o nível: '))

    if(nivel == 1):
        total_de_tentativas = 202
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range (1, total_de_tentativas + 1):
        print(f'Tentativa {rodada} de {total_de_tentativas}')
        palpite = input('Digite um número de 1 a 100: ')
        print ('Você digitou', palpite)
        palpite = int(palpite)

        if palpite < 1 and palpite > 100:
            print('Vc deve digitar um número entre 1 e 100')
            continue

        acertou = numero_secreto == palpite
        maior = palpite > numero_secreto
        menor = palpite < numero_secreto

        if acertou:
            print (f'Você acertou e fez {pontos} pontos! :)')
            break 
        else:
            if maior:
                print ('Você errou, seu chute foi maior que o número secreto')
            elif menor:
                print ('Você errou, seu chute foi menor que o número secreto')
            pontos_perdidos = abs(numero_secreto - palpite)    
            pontos = pontos - pontos_perdidos


if(__name__ == '__main__'):
    jogar()