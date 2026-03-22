# ler ano de nscimento da pessoa, dizer se ele ainda vai se alistar ao servico militar, se é a hora de se alistar ou
# se ja passou o tempo do alistamento.. mostrar quanto tempo falta ou quanto tempo ja passou do alistamento.

from datetime import date

nasc = int(input('Ano de nascimento: '))
idade = date.today().year - nasc

if idade < 18:
    tempo = 18 - idade
    print(f'Você deverá se alistar em {tempo} anos!')
elif idade == 18:
    print('Já é ano de alistar ao serviço militar!')
else:
    tempo = idade - 18
    print(f'Você já se alistou tem {tempo} anos!')