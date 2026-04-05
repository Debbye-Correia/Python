n = s = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')

# Alinhando
nome = 'Jose'
idade = 33
sal = 987.3
print(f'O {nome:-<20} tem {idade} anos e ganha R${sal:.2f}')
# O espaço do nome vai ocupar 20 casas, e vai colocar alinhar o nome na frente