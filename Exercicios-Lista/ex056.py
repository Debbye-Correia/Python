sidade = 0
velho = 0
menos20 = 0

for c in range (1,5):
    print('-=' * 25)
    nome = str(input(f'Digite o {c}º nome: '))
    idade = int(input(f'Idade de {nome}: '))
    sexo = str(input(f'Sexo [M] [F]: ')).upper()
    sidade += idade
    if sexo == 'M':
        if idade > velho:
            hvelho = nome
    elif sexo == 'F':
        if idade < 20:
            menos20 += 1
midade = sidade / 4
print(f'A media de idade do grupo é de {midade} anos de idade.')
print(f'O Homem mais velho se chama {hvelho}.')
print(f'Existem {menos20} Mulheres menores de 20 anos.')
