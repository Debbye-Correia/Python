elementos = []
c = 0
while True:
    elementos.append(int(input('Digite um valor: ')))
    c += 1
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if r == 'N':
        break
print('=-'*40)
print(f'Você digitou {c} elementos.')
elementos.sort(reverse=True)
print(f'Os valores em ordem decrescente são {elementos}')
if 5 in elementos:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')