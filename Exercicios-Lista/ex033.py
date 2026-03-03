# ler 3 numeros e mostrar qual é o maior e qual é o menor
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Agora o segundo numero: '))
n3 = int(input('E por fim o ultimo numero: '))

if n1 >= n2 and n1 >= n3:
    print (f'O maior numero é o {n1}')
else:
    if n2 >= n1 and n2 >= n3:
        print (f'O maior numero é o {n2}')
    else:
        print(f'O maior numero é o {n3}')

if n1 <= n2 and n1 <= n3:
    print (f'O menor numero é o {n1}')
else:
    if n2 <= n1 and n2 <= n3:
        print (f'O menor numero é o {n2}')
    else:
        print(f'O menor numero é o {n3}')