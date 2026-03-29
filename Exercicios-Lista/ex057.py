op = 1
s = ''
while op != 0:
    s = str(input('Digite o seu sexo: [M/F] ')).strip()
    if s in 'MFmf':
        print('Opção registrada com sucesso!')
        op = 0
    else:
        print('Opção inválida! Tente novamente!')
