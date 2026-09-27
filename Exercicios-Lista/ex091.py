from random import randint
jogo = dict()
ranking = list()
jogo['jogador1'] = randint(1,6)
jogo['jogador2'] = randint(1,6)
jogo['jogador3'] = randint(1,6)
jogo['jogador4'] = randint(1,6)
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'   O {k} tirou {v}')

ranking.append(jogo.copy())
for j in ranking:
    for v in j.values():
        if v


print()


print('Ranking dos jogadores: ')


