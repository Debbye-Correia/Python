n = int(input('Digite um numero: '))
div = 0
for c in range (1,n+1):
    if n % c == 0:
        div += 1
if div == 2:
    print('É um numero PRIMO')
else:
    print('NÃO É um numero PRIMO')
