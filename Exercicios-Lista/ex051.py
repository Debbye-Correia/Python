pt = int(input('Digite o primeiro termo da PA: '))
raz = int (input('Digite a razão da PA: '))
decimo = pt + (10 - 1) * raz
for c in range (pt, decimo + raz, raz):
    print(c, end=' ')
print('ACABOU.')


