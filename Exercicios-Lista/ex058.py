import random
num1 = random.randint(0,10)
r = False
t = 0
print('O PC sorteou um numero de 0 a 10. Será que você adivinha qual é?')
while not r:
    num2 = int(input('Qual o seu palpite? '))
    t += 1
    if num1 == num2:
        r = True
    else:
        if num2 < num1:
            print('Mais... Tente novamente! ', end=' ')
        else:
            print('Menos... Tente novamente! ', end=' ')
if t == 1:
    print('Você venceu na primeira tentativa! Parabens!')
else:
    print(f'Você venceu! Foram necessárias {t} tentativas!')