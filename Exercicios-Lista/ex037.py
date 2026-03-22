# pedir um numero inteiro e para o usuario escolher a base de conversao: 1 para binario, 2 para octal e 3 para
# hexadecimal
import numbers
num = int(input('Digite um numero aleatorio: '))
op = int(input('Para converter o numero em binario digite 1, para octal digite 2 e para hexadecimal digite 3: '))

if op == 1:
    print(f'A forma binaria do numero {num} é {bin(num)}')
elif op == 2:
    print(f'A forma octal do numero {num} é {oct(num)}')
elif op == 3:
    print(f'A forma hexadecimal do numero {num} é {hex(num)}')
else:
    print('Escolha inválida!')

