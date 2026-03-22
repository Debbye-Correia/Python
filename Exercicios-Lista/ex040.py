n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

media = (n1+n2)/2

if media < 5.0:
    print(f'REPROVADO! Media de {media:.1f}')
elif media < 7.0:
    print(f'RECUPERAÇÃO! Media de {media:.1f}')
else:
    print(f'APROVADO! Media de {media:.1f}')