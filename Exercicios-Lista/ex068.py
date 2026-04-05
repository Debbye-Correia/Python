from random import randint
v = 0
print('=-' * 20)
print(f'      VAMOS JOGAR PAR OU IMPAR')
print('=-' * 20)
while True:
    pc = randint (1,10)
    jo = int(input('Diga um valor: '))
    s = pc + jo
    jogo = str(input('Par ou Impar? [P/I] ')).upper().strip()[0]
    while jogo not in 'PpIi':
        jogo = str(input('Par ou Impar? [P/I] ')).upper().strip()[0]
    print('-' * 40)
    if s % 2 == 0:
        res = 'PAR'
    else:
        res = 'IMPAR'
    print(f'Você jogou {jo} e o PC jogou {pc}. Total de {s} DEU {res}')
    print('-' * 40)
    if jogo != res[0]:
        print('Você PERDEU!')
        break
    else:
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        v += 1
print('=-' * 20)
print(f'GAME OVER! Você venceu {v} vezes.')
