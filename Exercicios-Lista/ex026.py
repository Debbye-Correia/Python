# ler uma frase e dizer: quantas letras "A" tem, e qual é a primeira e ultima posição em que ela aparece
frase = str(input('Digite uma frase qualquer: ')).strip().lower()
print(f'Existem {frase.count('a')} letras "a" nesta frase.')
print(f'Aparece pela primeira vez na posição {frase.find('a')}, e pela ultima na posição '
      f'{frase.rfind('a')}.')