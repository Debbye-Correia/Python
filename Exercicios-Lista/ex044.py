prod = float(input('Valor do produto: R$'))

op = int(input('MODO DE PAGAMENTO: '
               '1 - A vista no dinheiro/cheque '
               '2 - A vista no cartão '
               '3 - Até 2x no cartão '
               '4 - 3x ou mais no cartão '))
print('O valor final a ser pago é de: ')
if op == 1:
    valor = prod - (prod * 0.10)
    print(f'R$ {valor}')
elif op == 2:
    valor = prod - (prod * 0.05)
    print(f'R$ {valor}')
elif op == 3:
    print(f'R$ {prod}')
elif op == 4:
    valor = prod + (prod * 0.20)
    print(f'R$ {valor}')