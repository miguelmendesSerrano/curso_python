# Funções aprofundadas em Python
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mUsuário interrompeu a execução.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mUsuário interrompeu a execução.\033[m')
            return 0
        else:
            return n


num = leiaInt('Digite um número inteiro: ')
valor = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi \033[34m{num}\033[m e o valor real foi \033[34m{valor}\033[m')
