from random import randint
print('Vamos jogar JoKenPô')
pc = randint(1,3)
print('1 - Pedra , 2 - Papel, 3 - Tesoura')
jo = int(input('Digite o numero da sua opção:'))

if pc == jo:
    print('Empate!')
elif (pc == 1 and jo == 2) or (pc == 2 and jo == 3) or (pc == 3 and jo == 1):
    print('Você ganhou!')
else:
    print('Você Perdeu!')