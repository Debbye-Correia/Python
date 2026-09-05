teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
print(' ')
galeras = [['Joao', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galeras[2][1])
print(galeras[3][0])
print(galeras[1])
print(' ')
print('Dados da galera:')
for p in galeras:
    print(p[0], 'tem', p[1], 'anos de idade')
print(' ')

galera3 = list()
dado = list()
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append((int(input('Idade: '))))
    galera3.append(dado[:])
    dado.clear()
print(galera3)
print(' ')

totmai = totmen = 0
for p in galera3:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')

