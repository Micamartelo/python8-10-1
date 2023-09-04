primeiro = int(input('Primeiro Termo:'))
razão = int(input('Razão:'))
termo = primeiro
contador = 1
while contador <= 10:
    print(termo)
    termo += razão
    contador +=1
print('Fim!')
