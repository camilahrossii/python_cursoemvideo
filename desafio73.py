print('-='*30)
listaTimes = ('Palmeiras', 'Bragantino' ,'Santos' ,'São Paulo', 'Vasco da Gama', 'América-MG',
              'Athletico-PR', 'Atlético-MG', 'Bahia', 'Botafogo', 'Corinthians', 'Coritiba',
              'Goiás', 'Grêmio', 'Cruzeiro', 'Cuiabá', 'Flamengo', 'Fluminense', 'Fortaleza',  'Internacional')
print(f'Lista de times do Brasileirão 2023: {listaTimes}')
print('-='*30)
print(f'Os 5 primeiros são {listaTimes[0:5]}')
print('-='*30)
print(f'Os 4 últimos são {listaTimes[-5:]}')
print('-='*30)
print(f'Times em ordem alfabética: {sorted(listaTimes)}')
print('-='*30)
print(f'O Coritiba está na {listaTimes.index("Coritiba")+1}ª posição')
