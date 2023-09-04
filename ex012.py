respo = 'S'
numero = 0
media = 0
while respo in 'Ss' :
    num = int(input('Digite um número iteiro'))
    Sn = str(input('Quer continuarl, digite [S/N]')).strip().upper()
    numero = num + numero
    media = (numero)/numero
    if Sn == 'N':
        print('{} total e {} media Fim!'.format(numero,media))