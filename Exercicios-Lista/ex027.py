# ler o nome completo de uma pessoa e mostrar o primeiro e ultimo nome separadamente
nome = str(input('Digite um nome completo: ')).strip()
div = nome.split()
print(f'O primeiro nome é: {div[0]}')
print(f'O ultimo nome é: {div[len(div)-1]}') # resolução do prof
