lista = []
pares = []
impares = []
while True:
    v = int(input('Digite um valor: '))
    lista.append(v)
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if r == 'N':
        break

print('=-'*40)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')
