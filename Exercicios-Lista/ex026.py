# ler uma frase e dizer: quantas letras "A" tem, e qual é a primeira e ultima posição em que ela aparece
frase = str(input('Digite uma frase qualquer: '))
print(f'Existem {frase.lower().count('a')} letras "a" nesta frase.')
print(f'Aparece pela primeira vez na posição {frase.lower().find('a')}, e pela ultima na posição '
      f'{frase.lower().rfind('a')}.')