from random import randint
sort = (randint(0,9), randint(0,9),randint(0,9) ,randint(0,9), randint(0,9))
print(f'Os valores sorteados foram:', end=' ')
for s in sort:
    print(f'{s}', end=' ')
print(f'\nO maior valor sorteado foi {max(sort)}')
print(f'O menor valor sorteado foi {min(sort)}')