# ler 4 nomes de alunos e sortear aleatoriamente
from random import choice
n1 = str(input('Digite o nome do 1º aluno: '))
n2 = str(input('Digite o nome do 2º aluno: '))
n3 = str(input('Digite o nome do 3º aluno: '))
n4 = str(input('Digite o nome do ultimo aluno: '))

nomes = [n1, n2, n3, n4]
escolhido = choice(nomes)
print(f'O aluno escolhido foi {escolhido}')