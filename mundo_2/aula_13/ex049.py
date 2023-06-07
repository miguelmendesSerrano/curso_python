# Tabuada v.2.0
n = int(input('Digite um número inteiro para ver sua tabuada: '))
print('=' * 12)
for i in range(1, 11):
    print('\033[34m{}\033[m x {:2} = \033[32m{}\033[m'.format(n, i, n * i))
print('=' * 12)
