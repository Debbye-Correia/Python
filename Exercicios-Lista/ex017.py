# ler o comprimento do cateto oposto e o do cateto adjacente de um triangulo retangulo
# e calcule o comprimento da hipotenusa
# o quadrado da hipotenusa é igual a soma dos quadrados dos catetos
import math
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
h = math.hypot(co, ca)
print(f'O valor da hipotenusa é de {h}')