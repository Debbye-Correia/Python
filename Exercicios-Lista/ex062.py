pa = int(input('Digite o primeiro termo da PA: '))
raz = int (input('Digite a razão da PA: '))
c = 0
print(f'[{pa}]', end=' ')
while c != 9:
    pa += raz
    print(f'[{pa}]', end=' ')
    c += 1
r = 1
while r != 0:
    r = int(input('\nQuer mostrar mais termos? Quantos? '))
    for i in range(r):
        pa += raz
        print(f'[{pa}]', end=' ')
