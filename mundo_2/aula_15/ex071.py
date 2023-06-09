# Simulador de Caixa Eletrônico
from time import sleep
ced_50 = ced_25 = ced_10 = ced_1 = 0
print('{:=^30}'.format(' BANCO 24 HORAS '))
valor = int(input('Qual valor quer sacar? R$'))
print('PROCESSANDO...')
sleep(1)
while valor != 0:
    if valor >= 50:
        valor -= 50
        ced_50 += 1
    elif valor >= 20:
        valor -= 20
        ced_25 += 1
    elif valor >= 10:
        valor -= 10
        ced_10 += 1
    else:
        valor -= 1
        ced_1 += 1
if ced_50 > 0:
    print(f'Total de {ced_50} cédulas de R$50.00')
if ced_25 > 0:
    print(f'Total de {ced_25} cédulas de R$20.00')
if ced_10 > 0:
    print(f'Total de {ced_10} cédulas de R$10.00')
if ced_1 > 0:
    print(f'Total de {ced_1} cédulas de R$1.00')
print('Obrigado por utilizar nossos serviços. Tenha um bom dia!')
