# ler 3 numeros e mostrar qual é o maior e qual é o menor
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Agora o segundo numero: '))
n3 = int(input('E por fim o ultimo numero: '))

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print (f'O menor numero é o {menor}')
print(f'O maior numero é o {maior}')