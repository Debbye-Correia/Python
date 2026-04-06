lanche = ('Hamburger', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(lanche[1])
print(lanche[3])
print(lanche[-2])
print(lanche[1:3])
print(lanche)
print(lanche[2:])
print(lanche[:2])
print(lanche[-3:])
#TUPLAS SAO IMUTAVEIS
# lanche[1] = 'Refrigerante'
print(lanche[1])

print(' ')

for c in lanche:
    print(f'Eu vou comer {c}')
print('Comi para caramba!')

print(' ')

for c in range (0, len(lanche)):
    print(f'Eu vou comer {lanche[c]} na posição {c}')
print('Comi para caramba!')

print(' ')
# Usando enumerate para saber a posicao
for pos, c in enumerate (lanche):
    print(f'Eu vou comer {c} na posição {pos}')
print('Comi para caramba!')
print(' ')
# 'sorted' vai ordenar alfabeticamente para exibição, porem nao vai mudar a TUPLA!
print(sorted(lanche))
print(lanche)

print(' ')
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
d = b + a
print(c)
print(d)
print(f'O numero 5 aparece na tupla C {c.count(5)} vezes')
print(c.index(5))
print(c.index(5,1))

print(' ')
# Tuplas aceitam varios tipos de dados diferentes
pessoa = ('Gustavo', 39 , 'M', 99.88)
print(pessoa)
del(pessoa)
print(pessoa)