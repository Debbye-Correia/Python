# programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiusculas
# O nome com todas as letras minusculas
# Quantas letras ao todo sem considerar os espaços
# Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: '))
print(f'O nome com todas as letras maiusculas: {nome.upper()}')
print(f'O nome com todas as letras minusculas: {nome.lower()}')
div = nome.split()
junto = ''.join(div)
print(f'Quantas letras ao todo sem considerar os espaços?  {len(junto)}')
primeironome = div[0]
print(f'Quantas letras tem o primeiro nome?  {len(primeironome)} ')