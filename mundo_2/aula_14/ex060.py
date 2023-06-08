# Cálculo do Fatorial
num = int(input('Digite um número: '))
count = num
f = 1
print('{}! = '.format(num), end='')
while count > 0:
    print('{}'.format(count), end='')
    print(' x ' if count > 1 else ' = ', end='')
    f *= count
    count -= 1
print('{}'.format(f))
