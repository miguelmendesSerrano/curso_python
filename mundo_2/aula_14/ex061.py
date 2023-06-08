# Progressão Aritmética v2.0
print('=' * 13)
print('Gerador de PA')
print('=' * 13)
num = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
count = 0
while count < 10:
    print('{} --> '.format(num), end='')
    num += r
    count += 1
print('Fim')
