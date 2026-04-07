nums = (int(input('Digite um numero: ')), int(input('Digite outro numero: ')), int(input('Digite mais um numero: ')),
      int(input('Digite o ultimo numero: ')))
print(f'Você digitou os valores {nums}')
print(f'O valor 9 apareceu {nums.count(9)} vezes')
if 3 not in nums:
    print('O valor 3 não foi digitado em nenhuma posição')
else:
    print(f'O valor 3 foi digitado na {nums.index(3)+1}ª posição ')
print('Os valores pares digitados foram:', end=' ')
for c in nums:
    if c % 2 == 0:
        print(c, end=' ')