# 5! = 5 * 4 * 3 * 2 * 1 = 120
n = int(input('Digite um numero: '))
c = n - 1
f = n * c
c = c-1
while c != 1:
    f *= c
    c -= 1
print(f'O fatorial do numero {n} é {f}')