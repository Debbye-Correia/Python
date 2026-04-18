lista = list()
for c in range (0,5):
    #lista.append(int(input('Digite um valor: ')))
    v = int(input('Digite um valor: '))
    if c == 0: # 0
        lista.insert(4,v)
        print('Adicionado ao final da lista...')
    elif c == 1: # 0 1
        if v > lista[0]:
            lista.insert(4, v)
            print('Adicionado ao final da lista...')
        elif v < lista[0]:
            lista.insert(0,v)
            print('Adicionado na posição 0 da lista...')
    elif c == 2: # 0 1 2
        if v > lista[1]:
            lista.insert(4, v)
            print('Adicionado ao final da lista...')
        elif v < lista[0]:
            lista.insert(0,v)
            print('Adicionado na posição 0 da lista...')
        else:
            lista.insert(1,v)
            print('Adicionado na posição 1 da lista...')
    elif c == 3: # 0 1 2 3
        if v > lista[2]:
            lista.insert(4, v)
            print('Adicionado ao final da lista...')
        elif v < lista[0]:
            lista.insert(0,v)
            print('Adicionado na posição 0 da lista...')
        elif v > lista[1]:
            lista.insert(2,v)
            print('Adicionado na posição 2 da lista...')
        else:
            lista.insert(1,v)
            print('Adicionado na posição 1 da lista...')
    elif c == 4:
        if v > lista[3]:
            lista.insert(4, v)
            print('Adicionado ao final da lista...')
        elif v < lista[0]:
            lista.insert(0,v)
            print('Adicionado na posição 0 da lista...')
        elif v > lista[2]:
            lista.insert(3,v)
            print('Adicionado na posição 3 da lista...')
        elif v > lista[1]:
            lista.insert(2,v)
            print('Adicionado na posição 2 da lista...')
        else:
            lista.insert(1,v)
            print('Adicionado na posição 1 da lista...')
print('-='*30)
print(f'Valores digitados em ordem foram {lista}')