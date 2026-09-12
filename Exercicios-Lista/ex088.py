jogos = list()
lista = list()
from random import randint
from time import sleep
print('-' * 40)
print(f'{'JOGOS DA MEGA SENA':^40}')
print('-' * 40)
qtd = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= qtd:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont+=1
        if cont >=6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f'{'-='*5} SORTEANDO {qtd} JOGOS {'-='*5}')
sleep(0.5)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print()
print(f'{'-='*5} < BOA SORTE! > {'-='*5}')



