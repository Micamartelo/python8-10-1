import random
computador = random.randint(0,10)
print('+++++Digite um valor enre (0 e 10), para você tentar adivinhar....Será que consegue?+++++')
acertou = False
while not acertou:
    jogador = int(input('+++++Digite um para tentar ganhar!+++++'))
    if jogador == computador:
        acertou == True
        print('Parabens você ganhou!')
    elif jogador != computador:
        print('Você PERDEU!')
print('Acabou!')
            