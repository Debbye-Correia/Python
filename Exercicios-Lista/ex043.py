peso = float(input('Digite seu peso em quilos: '))
alt = float(input('Digite sua altura em metros: '))
imc = peso / (alt * alt)
print(f'Com um IMC de {imc} o seu status é: ')
if imc < 18.5:
    print('Abaixo do peso!')
elif imc <= 25:
    print('Peso ideal!')
elif imc <= 30:
    print('Sobrepeso!')
elif imc <= 40:
    print('Obesidade!')
else:
    print('Obesidade mórbida!')