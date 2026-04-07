extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
           'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezecete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    n = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= n <= 20:
        print(f'Você digitou o numero {extenso[n]}')
    else:
        print('Tente novamente!', end=' ')
    r = str(input('Quer continuar? [S/N] ')).upper().strip()
    if r == 'N':
        break
print('FIM')