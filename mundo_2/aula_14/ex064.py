# Tratando vários valores v1.0
cont = soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite um número [999 para parar]: '))
print('O total foi de {} números digitados\nA soma entre eles é {}'.format(cont, soma))
