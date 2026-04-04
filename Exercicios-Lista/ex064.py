s = 0
n = 0
c = 0
while n != 999:
    n = int(input('Digite um valor: '))
    c += 1
    s += n
print(f'Foram digitados {c - 1} valores, e a soma dos valores é de {s - 999}')