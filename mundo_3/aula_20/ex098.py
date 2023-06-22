# Função de Contador
from time import sleep


def contador(start, stop, step):
    if step < 0:
        step *= -1
    if step == 0:
        step = 1
    print('=' * 30)
    print(f'Contagem de {start} até {stop} de {step} em {step}')
    sleep(1.5)

    if start < stop:
        cont = start
        while cont <= stop:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += step
        print('FIM!')
    else:
        cont = start
        while cont >= stop:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= step
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez!')
start = int(input('Ínicio: '))
stop = int(input('Fim: '))
step = int(input('Passo: '))
contador(start, stop, step)
