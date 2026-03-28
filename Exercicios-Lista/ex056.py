sidade = 0
velho = 0
menos20 = 0
hvelho = ''
for c in range (1,5):
    print(f'{'-=' * 5} {c}º Pessoa {'-=' * 5}')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    sidade += idade
    if c == 1 and sexo in 'Mm':
        velho = idade
        hvelho = nome
    if sexo in 'Mm' and idade > velho:
        hvelho = nome
        velho = idade
    if sexo in 'Ff' and idade < 20:
        menos20 += 1
midade = sidade / 4
print(f'A media de idade do grupo é de {midade} anos de idade.')
print(f'O Homem mais velho tem {velho} anos de idade e se chama {hvelho}.')
print(f'Existem {menos20} Mulheres menores de 20 anos.')
