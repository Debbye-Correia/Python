# Aluguel de carros: pedir a quantidade de dias que o carro foi alugado, os km rodados e dar o total a pagar
# R$ 60.0 por dia
# R$ 0.15 por Km rodado

d = int(input('Quantidade de dias com o carro alugado: '))
km = float(input('Quantidade de Km rodados? '))
total = (d * 60) + (km * 0.15)
print(f'O valor total a ser pago é de R${total:.2f}')