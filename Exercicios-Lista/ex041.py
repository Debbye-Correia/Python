from datetime import date

nasc = int(input('Ano de nascimento: '))
idade = date.today().year - nasc

print('De acordo com a sua idade a sua categoria é: ')
if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('Junior')
elif idade <=20:
    print('Senior')
else:
    print('Master')