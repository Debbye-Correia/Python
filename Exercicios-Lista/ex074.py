from random import randint
sort = (randint(0,9), randint(0,9),randint(0,9) ,randint(0,9), randint(0,9))
print(f'Os valores sorteados foram: {sort}')
for c in range (0, len(sort)):
    if c == 0:
        menor = sort[c]
        maior = sort[c]
    if sort[c] < menor:
        menor = sort[c]
    elif sort[c] > maior:
        maior = sort[c]
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')