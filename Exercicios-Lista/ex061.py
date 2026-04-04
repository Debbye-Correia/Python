pa = int(input('Digite o primeiro termo da PA: '))
raz = int (input('Digite a razão da PA: '))
c = 1
while c <= 10:
    print(f'[{pa}]', end=' ')
    pa += raz
    c += 1
