from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
print('Vamos jogar JoKenPô')
pc = randint(0,2)
print('=' * 20)
print('''[0] Pedra 
[1] Papel
[2] Tesoura''')
jo = int(input('Qual você vai jogar? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('=' * 20)
print(f'''Computador jogou {itens[pc]}
Jogador jogou {itens[jo]}''')
print('=' * 20)
if pc == jo:
    print('Empate!')
elif (pc == 0 and jo == 1) or (pc == 1 and jo == 2) or (pc == 2 and jo == 0):
    print('Você ganhou!')
else:
    print('Você Perdeu!')