pa = int(input('Digite o primeiro termo da PA: '))
raz = int (input('Digite a razão da PA: '))
c = 0
print(f'[{pa}]', end=' ')
while c != 9:
    pa += raz
    print(f'[{pa}]', end=' ')
    c += 1



