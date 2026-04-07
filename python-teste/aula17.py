num = [2, 5, 9, 1]
print(f'Lista primaria {num}')
num[2]= 3
print(f'Trocando o item na 2ª posicao {num}')
num.append(7)
print(f'Adicionando um novo item {num}')
num.insert(2,0)
print(f'Iserindo um novo item na 2ª posicao {num}')
print(f'Lista em ordem crescente {sorted(num)}')
num.sort(reverse=True)
print(f'Lista em ordem decrescente {num}')
print(f'Essa lista contem {len(num)} elementos.')
print(' ')

valores = list()
for cont in range (0,5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posicao {c} encontrei o valor {v}!')
print('Cheguei ao final da lista!')

