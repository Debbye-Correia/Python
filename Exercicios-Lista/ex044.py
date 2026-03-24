#   print(f'{:=^40} LOJINHA ') #NAO FUNCIONOU A FUNCAO PARA COLOCAR OS = COM O NOME CENTRALIZADO
prod = float(input('Valor do produto: R$'))

op = int(input('''MODO DE PAGAMENTO: 
1 - A vista no dinheiro/cheque 
2 - A vista no cartão 
3 - Até 2x no cartão 
4 - 3x ou mais no cartão 
Digite o numero correspondente: '''))
if op == 1:
    valor = prod - (prod * 0.10)
elif op == 2:
    valor = prod - (prod * 0.05)
elif op == 3:
    valor = prod
    parcela = valor / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f} sem juros!')
elif op == 4:
    valor = prod + (prod * 0.20)
    totparc = int(input('Quantas parcelas? '))
    parcela = valor / totparc
    print(f'Sua compra será parcelada em {totparc}x de R${parcela:.2f} com juros!')
else:
    print('OPÇÃO INVALIDA!')
print(f'Sua compra de R${prod:.2f} vai sair por R$ {valor:.2f} no final')