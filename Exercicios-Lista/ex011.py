#ler altura e largura de uma parede em metros, calcular sua area e a quantidade de tinta necessaria
#para pinta-la, sabendo que cada litro de tinta pinta uma area de 2m quadrados.
al = float(input('Quantos metros de altura tem a sua parede? '))
la = float(input('E quantos metros de largura? '))
area = al * la
t = area / 2
print(f'Para pintar uma area de {area} metros quadrados, será necessário {t} litros de tinta')
