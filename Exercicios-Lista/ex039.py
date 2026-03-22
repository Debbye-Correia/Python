# ler ano de nscimento da pessoa, dizer se ele ainda vai se alistar ao servico militar, se é a hora de se alistar ou
# se ja passou o tempo do alistamento.. mostrar quanto tempo falta ou quanto tempo ja passou do alistamento.

from datetime import date

nasc = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - nasc

if idade < 18:
    tempo = 18 - idade
    print(f'Você deverá se alistar em {tempo} anos!')
    ano = atual + tempo
    print(f'Seu ano de alistamento é em {ano}')
elif idade == 18:
    print('Você deve se alistar ao serviço militar IMEDIATAMENTE!')
else:
    tempo = idade - 18
    print(f'Você já deveria ter se alistado há {tempo} anos!')
    ano = atual - tempo
    print(f'Seu ano de alistamento foi em {ano}')