import random

lista = list()
cont = 0

while True:
    num = random.randint(1, 60)
    if num not in lista:
        lista.append(num)
        cont += 1
    if cont >= 6:
        break
print(f'\nOs números sorteados foram {lista}')