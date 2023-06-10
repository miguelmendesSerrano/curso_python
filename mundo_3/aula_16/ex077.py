# Contando vogais em Tupla
lista_palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar')
for palavra in lista_palavras:
    print(f'\nNa palavra {palavra.upper()} temos: ', end='')
    for letra in palavra:
        if letra in 'aeiou':
            print(f'{letra.lower()}', end=' ')
