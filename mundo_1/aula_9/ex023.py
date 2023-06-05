# Separando dígitos de um número
num = int(input('Digite um número de 0 a 9999: '))
print('Unidade: {:1}\nDezena: {:2}\nCentena: {:1}\nMilhar: {:2}'.format(num // 1 % 10, num // 10 % 10, num // 100 % 10, num // 1000 % 10))
