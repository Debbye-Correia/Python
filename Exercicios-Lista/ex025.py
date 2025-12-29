# ler um nome e dizer se tem "Silva" no nome
nome = str(input('Digite um nome completo: ')).strip()
print(f'Existe o sobrenome "Silva" neste nome? {'Silva' in nome.title()}')
print(f'Se sim, em qual posição? {nome.title().find('Silva')}')