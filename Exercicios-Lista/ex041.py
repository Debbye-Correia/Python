from datetime import date

nasc = int(input('Ano de nascimento: '))
idade = date.today().year - nasc

print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('Categoria: Mirim')
elif idade <= 14:
    print('Categoria: Infantil')
elif idade <= 19:
    print('Categoria: Junior')
elif idade <=25:
    print('Categoria: Senior')
else:
    print('Categoria: Master')