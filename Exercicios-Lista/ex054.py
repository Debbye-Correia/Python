from datetime import date
atual = date.today().year
menor = 0
maior = 0
for c in range (1,8):
    nasc = int(input(f'Data de nascimento da {c}º pessoa: '))
    idade = atual - nasc
    if idade < 21:
        menor += 1
    else:
        maior += 1
print(f'Existem {menor} pessoas que ainda não atigiram a maioridade,\ne {maior} pessoas que já são maiores de idade.')