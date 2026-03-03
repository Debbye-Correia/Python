# ler um ano e mostrar se ele é bissexto ou não
ano = int(input('Digite um ano: '))
if ano % 4 == 0:
    print('É um ano Bissexto!')
else:
    print('Não é um ano Bissexto!')