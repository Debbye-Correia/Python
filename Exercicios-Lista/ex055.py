maior = 0
menor = 10000
for c in range (1,6):
    peso = float(input(f'Digite o peso da {c}º pessoa: [Kg] '))
    if peso < menor:
        menor = peso
    elif peso > maior:
        maior = peso
print(f'O maior peso registrado foi de {maior}Kg')
print(f'O menor peso registrado foi de {menor}Kg')
