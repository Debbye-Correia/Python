# ler um ano e mostrar se ele é bissexto ou não
ano = int(input('Que ano quer analisar? Digite 0 para analisar o ano atual: '))
from datetime import date
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} Bissexto!')
else:
    print(f'O ano {ano} NÃO é Bissexto!')