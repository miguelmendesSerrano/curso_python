# Tuplas com Times de Futebol
lista_times = ('Botafogo', 'Palmeiras', 'Atlético MG', 'Grêmio', 'Flamengo', 'Fluminense', 'Atlético PR',
               'São Paulo', 'Fortaleza', 'Cruzeiro', 'RB Bragantino', 'Santos', 'Internacional', 'Cuiaba',
               'Bahia', 'Corinthians', 'Goiás', 'América MG', 'Vasco', 'Coritiba')
print(lista_times)
print('=' * 40)
print(f'Os 5 primeiros são: {lista_times[0:5]}')
print('=' * 40)
print(f'Os 4 últimos são: {lista_times[-4:]}')
print('=' * 40)
print(sorted(lista_times))
print('=' * 40)
print(f' O Corinthians está na {lista_times.index("Corinthians")+1}º posição')
