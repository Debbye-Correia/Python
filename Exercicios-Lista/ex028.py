#Escreva um programa que faça o pc pensar um numero de 0 a 5 e pec1a para o usuario tentar descobrir , dizendo ao fim
# se o usuario venceu ou perdeu
import random
num1 = random.randint(0,5)
num2 = int(input('Tente adivinhar qual o numero de 0 a 5 que o PC sorteou:' ))
if num1 == num2:
    print('Você venceu!')
else:
    print(f'Você perdeu! O numero sorteado era {num1}!')

