num = 0
cont = 0
soma = 0
while  num != 990:
    num = int(input('Digite um numero [999 para parar]'))
    soma = soma + num
    cont = cont + 1
print('Você digitou {} números e a soma entre eles foi {}'.format(cont,soma))