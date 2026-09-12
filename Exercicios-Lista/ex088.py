jogo = []
lista = list()
from random import randint
from time import sleep
print('-' * 40)
print(f'{'JOGOS DA MEGA SENA':^40}')
print('-' * 40)
qtd = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'{'-='*5} SORTEANDO {qtd} JOGOS {'-='*5}')
for q in range(qtd):
    for n in range(0,6):
        v = randint(1,60)
        jogo.append(v)
    lista.append(jogo[:])
    jogo.clear()
#sleep(2)
for j in range(lista):
    print(f'Jogo {j+1}: {lista[j]} ', end='')
   # sleep(2)
print()
print(f'{'-='*5} < BOA SORTE! > {'-='*5}')



