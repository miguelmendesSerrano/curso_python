# Criando um Menu de Opções
from time import sleep
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
opcao = 0
while opcao != 5:
    opcao = int(input('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
    > Escolha uma das opções: '''))
    if opcao == 1:
        print('A soma de {} + {} = {}'.format(n1, n2, n1 + n2))
    elif opcao == 2:
        print('O resultado de {} x {} = {}'.format(n1, n2, n1 * n2))
    elif opcao == 3:
        if n1 > n2:
            print('O número {} é maior que {}'.format(n1, n2))
        elif n2 > n1:
            print('O número {} é maior que {}'.format(n2, n1))
        else:
            print('Os números são iguais.')
    elif opcao == 4:
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Oção inválida! Tente novamente')
    sleep(1.5)
print('Finalizado com sucesso.')
