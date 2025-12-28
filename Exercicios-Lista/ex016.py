#ler um numero real e mostrar sua porção inteira
import math
n = float(input('Digite um numero real: '))
i = math.trunc(n)
print(f'A parte inteira de {n} é {i}')