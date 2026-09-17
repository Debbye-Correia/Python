# lista = [[nome],[[n1],[n2]],[med]]
aluno = list()
nota = list()
boletim = list()
from time import sleep

print('-='*5, 'CADASTRO ALUNOS', '-='*5)
while True:
    aluno.append(str(input('Nome: ')))
    nota.append(float(input('Nota 1: ')))
    nota.append(float(input('Nota 2: ')))
    aluno.append(nota[:]) #copiando as notas para o cadastro do aluno
    aluno.append((nota [0] + nota [1]) / 2) # calculando a media direto no cadastro do aluno
    boletim.append(aluno[:]) #copiando todos os dados do aluno, na lista de boletins
    aluno.clear() #limpando a lista de cadastro, para o proximo aluno
    nota.clear() #limpando a lista de cadastro, para o proximo aluno
    res = str(input('Quer continuar? [S/N] '))
    if res in 'Nn':
        break
print('-='*25)
print(f'{'No.':<4} {'NOME':<13} {'MÉDIA'}')
print('-'*30)
for pos, a in enumerate(boletim):
    print(f'{pos:<4} {boletim[pos][0]:<13}  {boletim[pos][2]:.1f}')
print('-'*30)
while True:
    No = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if No == 999:
        print('FINALIZANDO...')
        sleep(1)
        print('<<< VOLTE SEMPRE >>>')
        break
    else:
        print(f'As notas de {boletim[No][0]} são {boletim[No][1]}')
        print('-' * 50)


