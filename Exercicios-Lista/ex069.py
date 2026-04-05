mais18 = hom = mumenos20 = 0
while True:
    print('-' * 40)
    print(f'{' '*9} CADASTRE UMA PESSOA')
    print('-' * 40)
    i = int(input('Idade: '))
    s = str(input('Sexo: [M/F] ')).upper().strip()[0]
    while s not in 'MFmf':
        s = str(input('Sexo: [M/F] ')).upper().strip()[0]
    if i > 18:
        mais18 += 1
    if s in 'Mm':
        hom += 1
    if s in 'Ff' and i < 20:
        mumenos20 += 1
    print('-' * 40)
    res = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while res not in 'SsNn':
        res = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if res in 'Nn':
        break
print(f'{'='*12} FIM DO PROGRAMA {'='*12}')
print(f'Total de pessoas com mais de 18 anos: {mais18}')
print(f'Ao todo temos {hom} homens cadastrados')
print(f'E temos {mumenos20} mulheres com menos de 20 anos')