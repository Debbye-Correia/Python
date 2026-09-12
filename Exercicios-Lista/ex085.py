num = [[],[]]
v = 0
for i in range(1,8):
    v = int(input(f'Digite o {i}o. valor: '))
    if v % 2 == 0:
        num[0].append(v)
    else:
        num[1].append(v)
num[0].sort()
num[1].sort()
print('=-'*30)
print(f'O valores pares digitados foram: {num[0]}')
print(f'Os valores impares digitados foram: {num[1]}')
