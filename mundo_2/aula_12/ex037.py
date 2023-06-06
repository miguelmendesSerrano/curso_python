# Conversor de Bases Numéricas
import math
num = int(input('Digite um múmero inteiro: '))
print('''Escolha uma das bases para converter:
\033[34m[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL\033[m''')
opcao = int(input('Sua opção: '))
# checando opção e convertendo numero
if opcao == 1:
    print('\033[33m{}\033[m convertido para binário é: \033[32m{}\033[m'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('\033[33m{}\033[m convertido para OCTAL é : \033[32m{}\033[m'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('\033[33m{}\033[m convertido para HEXADECIMAL é \033[32m{}\033[m'.format(num, hex(num)[2:]))
else:
    print('\033[m31Opção inválida!\033[m')
