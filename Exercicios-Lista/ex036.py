# pedir valor da casa, salario do comprador e qtd de anos q ele vai pagar. calcular orestacao mensal sabendo que ela
# nao pode exceder 30% do salario ou entao emprestimo negado.

casa = float(input('Quanto custa a casa que você gostaria de comprar? R$'))
sal = float(input('Qual é o seu salario atual? R$'))
anos = int(input('Em quantos anos você pretende pagar a casa? '))

mensal = casa / (anos * 12)
p100 = sal * 0.30
if p100 < mensal:
    print(f'EMPRESTIMO NEGADO! Infelizmente o valor maximo da prestação que você pode assumir é de R${p100:.2f} e na '
          f'simulacao atual a prestação esta saindo por R${mensal:.2f}')
else:
    print(f'EMPRESTIMO APROVADO! A sua prestação mensal será de R${mensal:.2f}')

