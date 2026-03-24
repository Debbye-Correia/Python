import sympy.polys.subresultants_qq_zz

pt = int(input('Digite o primeiro termo da PA: '))
raz = int (input('Digite a razão da PA: '))
for c in range (1, 11):
    pa = pt+(c-1)*raz
    print(f'[{pa}] ', end='')
print('ACABOU.')


