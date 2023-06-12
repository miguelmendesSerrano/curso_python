# Extraindo dados de uma lista
lista_num = []
while True:
    valor = int(input('Digite um valor: '))
    lista_num.append(valor)
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
lista_num.sort(reverse=True)
print(f'Você digitou {len(lista_num)} elementos.')
print(f'Os valores em ordem decrescente são {lista_num}')
if 5 in lista_num:
    print(f'O valor 5 faz parte da lista e está na {lista_num.index(5)+1}º posição')
else:
    print('O valor 5 não faz parte da lista')
