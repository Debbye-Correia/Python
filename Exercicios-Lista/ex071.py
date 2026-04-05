q50 = q20 = q10 = q1 = 0
print('=' * 40)
print(f'{' '*10} CAIXA ELETRONICO')
print('=' * 40)
v = int(input('Que valor você quer sacar? R$'))
while True:
    q50 = v / 50
    v -= (q50 * 50)
    q20 = v / 20
    v -= (q20 * 20)
    q10 = v / 10
    v -= (q10 * 10)
    q1 = v / 1
    v -= (q1 * 1)
    if v == 0:
        break
print(f'Total de {q50} cédulas de R$50')
print(f'Total de {q20} cédulas de R$20')
print(f'Total de {q10} cédulas de R$10')
print(f'Total de {q1} cédulas de R$1')
print('=' * 40)
print('Volte sempre! Tenha um bom dia!')