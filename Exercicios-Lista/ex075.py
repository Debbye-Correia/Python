n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
n3 = int(input('Digite mais um numero: '))
n4 = int(input('Digite o ultimo numero: '))
nums = (n1, n2, n3, n4)
print(f'Você digitou os valores {nums}')
print(f'O valor 9 apareceu {nums.count(9)} vezes')
if 3 not in nums:
    print('O valor 3 não foi digitado em nenhuma posição')
else:
    for pos, c in enumerate(nums):
        if c == 3:
            print(f'O valor 3 foi digitado na {pos+1}ª posição ')
print('Os valores pares digitados foram:', end=' ')
for c in nums:
    if c % 2 == 0:
        print(c, end=' ')