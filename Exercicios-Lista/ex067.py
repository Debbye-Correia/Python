while True:
    print('-' * 40)
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 40)
    if n < 0:
        print('ENCERRANDO...')
        break
    for i in range (1, 11):
        print(f'{n} x {i} = {n * i}')
print('PROGRAMA ENCERRADO!')
