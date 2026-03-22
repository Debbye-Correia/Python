# pedir 2 numeros e mostrar msg se: o primeiro valor é maior, o segundo valor é maior ou nao existe valor maior,
# os dois sao iguais

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

if n1 == n2:
    print('Não existe valor maior, os dois numeros são iguais!')
elif n1 > n2:
    print('O primeiro valor é maior!')
else:
    print('O segundo valor é maior!')