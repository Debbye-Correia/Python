#programa que leia quanto dinheiro uma pessoa tem na carteira e mostra quantos dolares ela pode comprar
#considerando 1 dolar = 3.27
r = float(input('Quanto dinheiro você tem na carteira? R$'))
d = r / 3.27
print(f'Com R${r:.2f} você pode comprar US${d:.2f}')