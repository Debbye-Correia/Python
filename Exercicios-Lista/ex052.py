n = int(input('Digite um numero: '))
div = 0
for c in range (1,n+1):
    if n % c == 0:
        print('\033[33m', end=' ')
        div += 1
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')
print(f'\n\033[m O numero {n} foi divisivel {div} vezes!')
if div == 2:
    print('E por isso ele É um numero PRIMO')
else:
    print('E por isso ele NÃO É um numero PRIMO')
