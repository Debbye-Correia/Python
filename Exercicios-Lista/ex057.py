s = str(input('Digite o seu sexo: [M/F] ')).strip().upper()[0]
while s not in 'MFmf':
    s = str(input('Opção inválida! Tente novamente! Digite o seu sexo: [M/F] ')).strip().upper()[0]
print(f'Sexo {s} registrado com sucesso!')