s = n = c = 0
n = int(input('Digite um valor [999 para parar]: '))
while n != 999:
    c += 1
    s += n
    n = int(input('Digite um valor [999 para parar]: '))
print(f'Foram digitados {c} valores, e a soma dos valores é de {s}')