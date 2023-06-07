# Detector de Palíndromo
frase = str(input('Digite uma frase: ')).strip().upper()
junto = frase.replace(' ', '')
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if junto == inverso:
    print('O inverso da frase: \033[34m{}\033[m é: \033[33m{}\033[m\nEntão é um Palíndromo.'.format(junto, inverso))
else:
    print('O inverso da frase: \033[34m{}\033[m é: \033[33m{}\033[m\nEntão não é um Palíndromo'.format(junto, inverso))
