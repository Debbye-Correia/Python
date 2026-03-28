# Exemplo 1
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim!')

# Exemplo 2
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
    print('Fim!')

# Exemplo 3
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 = 0
            par += 1
        else:
            impar += 1
print(f'Voce digitou {par} numeros pares e {impar} numero impares')