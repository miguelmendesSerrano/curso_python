# Contagem regressiva
from time import sleep
from emoji import emojize
for n in range(10, -1, -1):
    print('\033[34m{}\033[m'.format(n))
    sleep(1)
print(emojize('\033[31mDecolar !!!\033[m🚀'))
