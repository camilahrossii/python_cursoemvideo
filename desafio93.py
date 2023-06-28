jogador = {}
jogador['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou?  '))
partidas = []
for c in range(0, tot):
    partidas.append(int(input(f'     Quantos gols na partida {c+1}?  ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('=-' * 30)
print(jogador)
print('=-' * 30)
for k, v in jogador.items():
    print(f'{k}:  {v}')
print('=-' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
print('-' * 40)
for i, v in enumerate(jogador['gols']):
    print(f'    =>  Na partida {i+1}, fez {v} gols.')
print('-' * 40)
print(f'Total de {jogador["total"]} gols.')