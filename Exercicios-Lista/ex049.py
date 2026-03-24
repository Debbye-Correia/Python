from time import sleep
n = int(input('Você deseja a tabuada de qual numero? '))
print('Calculando...')
sleep(1)
print('-'*20)
print(f'>>>> TABUADA DE {n} <<<<  ')
for c in range (1,11):
    print(f'{n} X {c:2} = {n * c}')
print('-'*20)