pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas['nome'])
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.') #dentro dos colchetes foi necessario usar aspas duplas,
# pq já entamos em uam estrutura de aspas simples.
print()
print(pessoas.keys()) #para mostrar as chaves
print(pessoas.values()) #para mostrar os valores/informacoes cadastradas
print(pessoas.items()) #na exibicao podemos ver que tudo esta em incluso em uma lista[], com cada chave e seu valor
# atribuido em uma tupla()
print()
for k, v in pessoas.items():
    print(f'{k} = {v}')
print()
pessoas['nome'] = 'Leandro' # Mudando o valor de uma chave
for k, v in pessoas.items():
    print(f'{k} = {v}')
print()
del pessoas['sexo'] #deletando uma chave
for k, v in pessoas.items():
    print(f'{k} = {v}')
print()
pessoas['Peso'] = 98.5 #Adicionando uma chave
for k, v in pessoas.items():
    print(f'{k} = {v}')

print()
print()

brasil = []
estado1 = {'uf':'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'uf':'São Paulo', 'sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(estado2)
print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])
brasil.clear()

print()
estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)
print()
for e in brasil: #laço para a lista
    for v in e.values(): #laço para o dicionario
        print(v, end=' ')
    print()
