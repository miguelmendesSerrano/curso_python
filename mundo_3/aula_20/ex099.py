# Função que descobre o maior
from time import sleep


def maior(*num):
    count = maior = 0
    print('=' * 50)
    print('Analisando os valores informados...')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.5)
        if count == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        count += 1
    print(f'Foram informados {count} valores ao todo.')
    print(f'O maior valores informado foi {maior}')


maior(2, 3, 4, 5)
maior(8, 7, 6)
maior(6)
maior()
