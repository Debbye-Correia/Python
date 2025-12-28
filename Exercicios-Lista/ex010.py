#programa que leia quanto dinheiro uma pessoa tem na carteira e mostra quantos dolares ela pode comprar
#considerando 1 dolar = 3.27
r = float(input('Quanto dinheiro você tem na carteira? '))
d = r / 3.27
print(f'Com {r} reais você pode comprar {d:.2f} dolares')