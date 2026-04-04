pa = int(input('Digite o primeiro termo da PA: '))
raz = int (input('Digite a razão da PA: '))
c = 1
tot = 0
res = 10
while res != 0:
    tot += res
    while c <= tot:
        print(f'[{pa}]', end=' ')
        pa += raz
        c += 1
    print('Pausa')
    res = int(input('Quer mostrar mais termos? Quantos? '))
print(f'Progressão finalizada com {tot} termos!')
