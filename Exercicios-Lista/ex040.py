n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

media = (n1+n2)/2

if media < 5.0:
    print(f'REPROVADO! Media de {media}')
elif media < 7.0:
    print(f'RECUPERAÇÃO! Media de {media}')
else:
    print(f'APROVADO! Media de {media}')