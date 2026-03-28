for c in range (1,6):
    peso = float(input(f'Digite o peso da {c}º pessoa: [Kg] '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso < menor:
            menor = peso
        if peso > maior:
            maior = peso
print(f'O maior peso registrado foi de {maior}Kg')
print(f'O menor peso registrado foi de {menor}Kg')
