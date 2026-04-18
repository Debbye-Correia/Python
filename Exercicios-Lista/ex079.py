valores = list()
while True:
    v = (int(input('Digite um valor: ')))
    if v in valores:
        print('Valor duplicado! Não vou adicionar...')
    else:
        valores.append(v)
        print('Valor adicionado com sucesso!')
    res = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if res == 'N':
        break
print('-='*30)
print(f'Você digitou os valores {sorted(valores)}')