r = 'S'
s = c = 0
while r == 'S':
    v = int(input('Digite um valor: '))
    r = str(input('Quer continuar a digitar valores? [S/N] ')).strip().upper()[0]
    s += v
    c += 1
    if c == 1:
        menor = maior = v
    elif v < menor:
        menor = v
    elif v > maior:
        maior = v
print(f'A media entre os {c} valores digitados é {(s/c):.2f}')
print(f'O menor valor digitado é {menor} e o maior é {maior}')