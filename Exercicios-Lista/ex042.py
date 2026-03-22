r1 = float(input('Digite a reta 1: '))
r2 = float(input('Digite a reta 2: '))
r3 = float(input('Digite a reta 3: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É possivel fazer um triangulo!')
    if r1 == r2 and r2 == r3:
        print('Triangulo do tipo equilatero, todos os lados são iguais!')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Triangulo do tipo isosceles, dois lados iguais!')
    else:
        print('Triangulo do tipo escaleno, todos os lados diferentes!')
else:
    print('Não é possivel fazer um triangulo!')
