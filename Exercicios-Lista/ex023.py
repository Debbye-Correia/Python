#ler um numero de 0 a 9999 e a mostre na tela cada um dos digitos separados
# ex: 1834
# unidade: 4 >> dezena: 3  >> centena: 8  >> milhar: 1

num = str(input('Digite un numero de 0 a 9999:  '))
print(f'Unidade: {num[3]}')
print(f'Dezena: {num[2]}')
print(f'Centena: {num[1]}')
print(f'Milhar: {num[0]}')
# Funciona se utilisar 4 numeros. ex: 0056, 0182, 3794, 0005.