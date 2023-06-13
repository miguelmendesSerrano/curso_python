# Listas com pares e ímpares
lista = [[], []]
for i in range(1, 8):
    num = int(input(f'Digite o {i}° número: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
lista[0].sort()
lista[1].sort()
print(f'A lista com o números pares é {lista[0]}')
print(f'A lista com os números ímpares é {lista[1]}')
