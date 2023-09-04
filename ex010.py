num = int(input('Quantos termos vc quer mostrar?:'))
t1 = 0
t2 = 1
contador = 3
while contador <= num:
    t3 = t1 + t2
    print('{}'.format(t3))
    t1 = t2 
    t2 = t3
    contador +=1
print('fim!')