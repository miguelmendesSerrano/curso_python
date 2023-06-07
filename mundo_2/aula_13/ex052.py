# Números Primos
num = int(input('Digite o número que quer verificar: '))
div = 0
for i in range(1, num + 1):
    if num % i == 0:
        print('\033[31m', end='')
        div += 1
    else:
        print('\033[34m', end='')
    print('{} '.format(i), end='')
print('\n\033[mO número {} foi dividido {} vezes.'.format(num, div))
if div == 2:
    print('Por isso ele é PRIMO.')
else:
    print('Por isso ele NÃO é primo.')
