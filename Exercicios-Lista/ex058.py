import random
num1 = random.randint(0,10)
r = 0
t = 1
num2 = int(input('Tente adivinhar qual o numero de 0 a 10 que o PC sorteou:' ))
while r == 0:
    if num1 != num2:
        num2 = int(input('Você perdeu! Tente novamente: '))
        t += 1
    else:
        if t == 1:
            print('Você venceu na primeira tentativa! Parabens!')
        else:
            print(f'Você venceu! Foram necessárias {t} tentativas!')
        r = 1