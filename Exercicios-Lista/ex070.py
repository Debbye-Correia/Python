mais1000 = tot = qtd = 0
print('-' * 40)
print(f'{' LOJINHA ': ^40} ')
print('-' * 40)
while True:
    prod = str(input('Nome do Produto: '))
    valor = float(input('Preço: R$'))
    qtd += 1
    tot += valor
    if valor > 1000:
        mais1000 += 1
    if qtd == 1 or valor < vbarato:
        pbarato = prod
        vbarato = valor
    res = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while res not in 'SsNn':
        res = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if res in 'Nn':
        break
print(f'{' FIM DO PROGRAMA ':-^40}')
print(f'O total da compra dos {qtd} produtos foi {tot:.2f}')
print(f'Temos {mais1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {pbarato} que custa R${vbarato:.2f}')
