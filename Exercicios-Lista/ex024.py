# ler o nome de uma cidade e dizer se ela começa ou não com o nome "Santo"
cidade = str(input('Digite o nome de uma cidade: ')).strip()
div = cidade.split()
teste = div[0]
print(f'A cidade começa com o nome Santo? {teste.capitalize() == 'Santo'}')

# resolução do professor abaixo:
# print(cidade[:5].upper() == 'SANTO')