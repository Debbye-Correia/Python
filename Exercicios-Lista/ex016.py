#ler um numero real e mostrar sua porção inteira
from math import trunc
n = float(input('Digite um numero real: '))
i = trunc(n)
print(f'A parte inteira de {n} é {i}')

# tbem seria possivel fazer com uma função interna do python int(n)