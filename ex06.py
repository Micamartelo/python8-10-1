print('Esse é um programa que ler dois valores e faz o que se pede...')
valor = float(input('Digite um valor:'))
valor2 = float(input('Digite um outro valor:'))
somar = valor + valor2
multiplicar = valor * valor2
falso = False
print('[1]Somar:')
print('[2]Multiplicar:')
print('[3]Maior:')
print('[4]Novos números:')
print('[5]Sair do programa:')
resposta = int(input('Digite sua opção:'))
while True:
    if resposta == 1:
        print(somar)
        break
    if resposta == 2:
        print(multiplicar)
        break
    if resposta == 3:  
        if valor > valor2:
            print('O maior valor é {}'.format(valor))
        if valor2 > valor:
            print('O maior valor é {}'.format(valor2))
        if valor2 == valor: 
            print('Os dois são valores iguais!')
        break
    if resposta == 4:
        valor = float(input('Digite um valor:'))
        valor2 = float(input('Digite um outro valor:'))
    if resposta == 5:
        print('Fim do programa!..................')
