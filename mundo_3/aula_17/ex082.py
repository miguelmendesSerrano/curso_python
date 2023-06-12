# Dividindo valores em várias listas
lista_valores = []
lista_par = []
lista_impar = []
while True:
    valor = int(input('Digite um valor: '))
    lista_valores.append(valor)
    if valor % 2 == 0:
        lista_par.append(valor)
    else:
        lista_impar.append(valor)
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opcao == "N":
        break
print(f'A lista completa é {lista_valores}')
print(f'A lista somente com os números pares é {lista_par}')
print(f'A lista somente com os números ímpares é {lista_impar}')
