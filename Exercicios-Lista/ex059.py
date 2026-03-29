n1 = float(input('Digite o 1º numero: '))
n2 = float(input('Digite o 2º numero: '))
op = 0
while op != 5:
    print(f'{'-='*5} OPÇÕES {'-='*5} ')
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Saber qual é o Maior')
    print('[4] Digitar novos numeros')
    print('[5] Sair do programa')
    op = int(input('Qual operação você deseja fazer? '))
    if op == 1:
        print(f'A soma entre {n1} e {n2} é de {n1+n2}')
    elif op == 2:
        print(f'A multiplicação entre {n1} e {n2} é de {n1*n2}')
    elif op == 3:
        if n1 == n2:
            print(f'Os numeros {n1} e {n2} são iguais! Não existe maior!')
        elif n1 > n2:
            print(f'O numero {n1} é maior que o numero {n2}')
        else:
            print(f'O numero {n2} é maior que o numero {n1}')
    elif op == 4:
        print('Digite novos numeros para continuar as operações.')
        n1 = float(input('Digite o 1º numero: '))
        n2 = float(input('Digite o 2º numero: '))
    elif op == 5:
        print('SAINDO DO PROGRAMA...')
    else:
        print('Opção invalida! Tente novamente!')
print('PROGRAMA FINALIZADO COM SUCESSO!')