primeiro = int(input('Primeiro Termo:'))
razão = int(input('Razão:'))
termo = primeiro
contador = 1
total = 0
mais = 10
while mais !=0:
    total = total + mais
    while contador <= total:
        print(termo)
        termo += razão
        contador +=1
    print('Pausa!')
    mais = int(input('Quantos termos você quer mostrar a mais?'))
print('Fim!')