# Progressão Aritmética
n = int(input('Primeiro termo: '))
r = int(input('Razão: '))
decimo = n + (10 - 1) * r
for i in range(n, decimo + r, r):
    print('{} '.format(i), end='-> ')
print('Fim')
