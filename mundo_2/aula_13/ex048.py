# Soma ímpares múltiplos de três
s = 0
c = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        s += n
        c += 1
print('A soma entre os \033[34m{}\033[m múltiplos de 3 no intervalo de 1 a 500 é: \033[32m{}\033[m'.format(c, s))
