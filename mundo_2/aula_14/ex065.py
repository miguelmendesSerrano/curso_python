# Maior e Menor valores
cont = soma = opcao = 0
while opcao != 'N':
    num = int(input('Digite um número: '))
    opcao = input('Quer continuar? [S/N]').upper().strip()
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print('Você digitou {} números e a média foi {:.2f}'.format(cont, soma / cont))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
