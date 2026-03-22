# pedir um numero inteiro e para o usuario escolher a base de conversao: 1 para binario, 2 para octal e 3 para
# hexadecimal

num = int(input('Digite um numero aleatorio: '))
op = int(input('''Escolha uma das bases para conversão:
[1] para BINARIO
[2] para OCTAL
[3] para HEXADECIMAL 
Sua opção: '''))

if op == 1:
    print(f'A forma binaria do numero {num} é {bin(num)[2:]}')
elif op == 2:
    print(f'A forma octal do numero {num} é {oct(num)[2:]}')
elif op == 3:
    print(f'A forma hexadecimal do numero {num} é {hex(num)[2:]}')
else:
    print('Escolha inválida!')

