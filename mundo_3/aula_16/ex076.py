# Lista de Preços com Tupla
lista_produtos = ('Lápis', 2.75,
                  'Borracha', 1.50,
                  'Caderno', 14.90,
                  'Caneta', 2.50,
                  'Mochila', 150.0,
                  'Livro', 30,
                  'Compasso', 5.9)
print('=' * 28)
print(f'{"LISTA DE PREÇOS":^30}')
print('=' * 28)
for pos in range(0, len(lista_produtos)):
    if pos % 2 == 0:
        print(f'{lista_produtos[pos]:.<20}', end='')
    else:
        print(f'R${lista_produtos[pos]:>6.2f}')
print('=' * 28)
