# ler o salario e calcular o aumento. superior de 1250 aumento de 10%, inferiores aumento de 15%.
sal = float(input('Digite seu salario: R$'))
if sal >= 1250:
    nsal = sal + (sal* 0.10 )
    print(f'O seu novo salario com o aumento de 10% será de R${nsal}')
else:
    nsal = sal + (sal *0.15)
    print(f'O seu novo salario com o aumento de 15% será de R${nsal}')


