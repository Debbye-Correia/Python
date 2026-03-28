print('-=' * 25)
print('Detector de Palíndromo')
print('-=' * 25)
frase = str(input('Digite uma frase: ')).upper().strip().split()
junto = ''.join(frase)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
    # podemos usar a tecnica de fatiamento tbem
    # inverso = junto[::-1]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um Palíndromo!')
else:
    print('Não é um Palíndromo!')

