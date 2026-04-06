extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
           'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezecete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    n = int(input('Digite um numero entre 0 e 20: '))
    if n < 0 or n > 20:
        print('Tente novamente!', end=' ')
    else:
        break
print(f'Você digitou o numero {extenso[n]}')