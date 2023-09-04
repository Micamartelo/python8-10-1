sexo = str(input('Coloque seu sexo')).strip().upper()
while sexo not in 'MmFf':
    sexo = str(input('Dado invalido. Digite novamente!')).strip().upper()
print('Dados coletados!...')
