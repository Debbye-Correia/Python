from random import randint
from time import sleep
from operator import itemgetter #Para poder ordernar um dicionario
jogo = {'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6)}
ranking = list()
print('='*5,'Valores sorteados','='*5)
for k, v in jogo.items():
    print(f'     O {k} tirou {v}')
    sleep(1)

ranking = sorted(jogo.items(),key=itemgetter(1), reverse=True) #É No.1 para poder ordenar pela chave 1 que são os numeros
# sorteados. Se fosse por No.0 ele ordenaria pela chave 0 que é o nome do jogador. Utilizamos o reverse=True para que
# ele ordene de forma decrescente e nao cresente.
print('='*5,'Ranking dos jogadores','='*5)
for i, v in enumerate(ranking):
    print(f'    {i+1}o lugar: {v[0]} com {v[1]}')
    sleep(1)