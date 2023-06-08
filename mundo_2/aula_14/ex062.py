# Super Progressão Aritmética v2.0
print('=' * 13)
print('Gerador de PA')
print('=' * 13)
num = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
count = 0
termo = num
total = 0
mais = 10
while mais != 0:
    total += mais
    while count < total:
        print('{} --> '.format(termo), end='')
        termo += r
        count += 1
    print('Pausa')
    mais = int(input('Quantos termos quer mostrar a mais? '))
print('Progressão finalizada. O total de termos mostrados foi {}.'.format(total))
