# ler nome de 4 alunos, sortear e mostrar a ordem em que eles farão a apresentação
from random import shuffle
n1 = input('Digite o nome do 1º aluno: ')
n2 = input('Digite o nome do 2º aluno: ')
n3 = input('Digite o nome do 3º aluno: ')
n4 = input('Digite o nome do ultimo aluno: ')

lista = [n1, n2, n3, n4]
shuffle(lista)
print('Ordem de apresentação:')
print(lista)
