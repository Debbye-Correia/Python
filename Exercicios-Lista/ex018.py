# ler um angulo qualquer e mostrar na tela o valor do seno, cosseno e tangente deste angulo
from math import sin, cos, tan, radians
a = float(input('Digite um angulo qualquer: '))
print(f'Seguem os valores de seno, cosseno e tangente do angulo {a}º ')
print(f'Seno: {sin(radians(a)):.2f}')
print(f'Cosseno: {cos(radians(a)):.2f}')
print(f'Tangente: {tan(radians(a)):.2f}')