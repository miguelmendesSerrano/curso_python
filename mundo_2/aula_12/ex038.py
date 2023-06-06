# Comparando números
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O \033[32mprimeiro\033[m número é maior.')
elif n2 > n1:
    print('O \033[32msegundo\033[m número é maior.')
else:
    print('Os números são iguais.')
