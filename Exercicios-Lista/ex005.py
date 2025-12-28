# Programa que leia um numero inteiro e calcule seu antecessor e seu sucessor
n = int(input('Digite um numero inteiro: '))
a = n - 1
s = n + 1
print(f'O antecessor de {n} é {a} e o sucessor é {s}')
# eu usei variaveis para calcular, mas poderia ter feito direto nos colchetes
# print(f'O antecessor de {n} é {n-1} e o sucessor é {n+1}')
# dessa forma economizamos memória, porém os valores não podem ser reutilizados posteriormente