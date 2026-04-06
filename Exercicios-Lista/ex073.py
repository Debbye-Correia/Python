times = ('Palmeiras', 'São Paulo', 'Fluminense', 'Flamengo', 'Bahia', 'Athletico-PR', 'Coritiba', 'Atlético-MG',
         'Red Bull Bragantino','Botafogo', 'Grêmio', 'Vasco da Gama', 'Internacional', 'Vitória', 'Santos',
         'Corinthians', 'Chapecoense', 'Remo', 'Cruzeiro', 'Mirassol')
print('-='*40)
print(f'Listas de times do Brasileirão: {times}')
print('-='*40)
print(f'Os 5 primeiros são {times[0:5]}')
print('-='*40)
print(f'Os 4 ultimos são {times[-4:]}')
print('-='*40)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*40)
print(f'O Chapecoense esta na {(times.index('Chapecoense')+1)}ª posição')
