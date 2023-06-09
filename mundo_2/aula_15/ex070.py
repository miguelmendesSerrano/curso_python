# Estatísticas em produtos
total_compra = produto_mil = menor = 0
barato = ''
print('=' * 25)
print('GAFANHOTO SUPERMERCADOS')
print('=' * 25)
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    total_compra += preco
    if preco > 1000:
        produto_mil += 1
    if total_compra == preco:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
print('{:=^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra é \033[32mR${total_compra:.2f}\033[m')
print(f'Temos \033[33m{produto_mil}\033[m produto(s) com preço acima de R$1000.00')
print(f'O produto mais barato foi a/o \033[34m{barato}\033[m que custa R${menor:.2f}')
